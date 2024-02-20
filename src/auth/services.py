import jwt
from core.db import get_db
from core.exceptions import UserAlreadyExist
from core.redis_repository import RedisRepository
from core.settings import SETTINGS
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from users.db_controller import UserDBController
from users.schemas import RegisterUser
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

    @staticmethod
    async def register_user(new_user: RegisterUser, db: AsyncSession = Depends(get_db)):
        db_user = await UserDBController.get_user_by_email(email=new_user.email, db=db)
        if db_user:
            raise UserAlreadyExist

        new_user.password = Hasher.get_password_hash(new_user.password)
        await RedisRepository.clear_key("users")
        return await UserDBController.register_user(new_user=new_user, db=db)
