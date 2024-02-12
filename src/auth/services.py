import jwt
from core.db import get_db
from core.settings import SETTINGS
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from users.db_controller import UserDBController
from users.services import UserService
from utils.hasher import Hasher


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


class AuthService:
    @staticmethod
    async def authenticate_user(email: str, password: str, db: AsyncSession):
        user = await UserDBController.get_user_by_email(email=email, db=db)
        if user is None:
            return
        if not Hasher.verify_password(password, user.password):
            return
        return user

    @staticmethod
    async def get_current_user_from_token(
        token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try:
            payload = jwt.decode(
                token, SETTINGS.SECRET_KEY, algorithms=[SETTINGS.ALGORITHM]
            )
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = await UserDBController.get_user_by_email(email=email, db=db)
        if user is None:
            raise credentials_exception
        return user
