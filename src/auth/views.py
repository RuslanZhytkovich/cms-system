from datetime import timedelta

from auth.schemas import Token
from auth.services import AuthService
from core.db import get_db
from core.security import create_access_token
from core.settings import SETTINGS
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User

login_router = APIRouter()


@login_router.post("/token", response_model=Token)
async def login_for_access_token(request: Request, db: AsyncSession = Depends(get_db)):
    form_data = await request.json()
    user = await AuthService.authenticate_user(
        form_data["username"], form_data["password"], db
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "other_custom_data": [1, 2, 3, 4]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@login_router.get("/test_auth_endpoint")
async def test_auth_endpoint(
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return {"Success": True, "current_user": current_user}
