from datetime import timedelta

from jose import jwt
from fastapi import APIRouter, Depends, HTTPException, Request, status, Form
from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import Token
from auth.services import AuthService
from core.db import get_db
from core.security import create_access_token, create_refresh_token
from core.settings import SETTINGS
from users.db_controller import UserDBController
from users.models import User
from users.schemas import RegisterUser

login_router = APIRouter()
register_router = APIRouter()


@login_router.post("/token", response_model=Token)
async def login_for_access_token(request: Request, db: AsyncSession = Depends(get_db),
                                 username: str = Form(...), password: str = Form(...)):
    user = await AuthService.authenticate_user(username, password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=SETTINGS.REFRESH_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email, "token_type": "access"},
        expires_delta=access_token_expires,
    )
    refresh_token = create_refresh_token(
        data={"sub": user.email, "token_type": "refresh"},
        expires_delta=refresh_token_expires,
    )

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@login_router.post("/token/refresh", response_model=Token)
async def refresh_access_token(refresh_token: str = Form(...), db: AsyncSession = Depends(get_db)):
    try:
        payload = jwt.decode(
            refresh_token, SETTINGS.SECRET_KEY, algorithms=[SETTINGS.ALGORITHM]
        )

        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный refresh токен",
            )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный refresh токен",
        )

    user = await UserDBController.get_user_by_email(email=email, db=db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не найден",
        )

    access_token_expires = timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "token_type": "access"},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


@login_router.get("/test_auth_endpoint")
async def auth_endpoint(current_user: User = Depends(AuthService.get_current_user_from_token)):
    return {"Success": True, "current_user": current_user}


@register_router.post("/register")
async def register_user(new_user: RegisterUser, db: AsyncSession = Depends(get_db)):
    return await AuthService.register_user(new_user=new_user, db=db)
