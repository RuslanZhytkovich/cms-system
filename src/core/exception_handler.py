from core.exceptions import AlreadyExist
from core.exceptions import DatabaseConnectionException
from core.exceptions import DatabaseException
from core.exceptions import UserAlreadyExist
from core.exceptions import InvalidCredentialsException
from core.exceptions import InvalidFileType
from core.exceptions import InvalidPermissionsException
from core.exceptions import InvalidTokenException
from core.exceptions import NotFoundException
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi import status
from fastapi.responses import JSONResponse


async def duplicate_entity_exception_handler(
    request: Request, exc: AlreadyExist
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Сущность с такими данными уже существует."},
    )


async def user_already_exist(
    request: Request, exc: AlreadyExist
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Пользователь с таким email уже существует."},
    )



async def not_found_exception_handler(
    request: Request, exc: NotFoundException
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": f"Не найдено.: {exc}"},
    )


async def invalid_credentials_exception_handler(
    request: Request, exc: InvalidCredentialsException
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Неверные реквизиты входа."},
    )


async def invalid_token_exception_handler(
    request: Request, exc: InvalidTokenException
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Неверный токен."}
    )


async def request_processing_exception_handler(
    request: Request, exc: DatabaseException | DatabaseConnectionException
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Пожалуйста попробуйте позже."}
    )


async def invalid_permissions_exception_handler(
    request: Request, exc: InvalidPermissionsException
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN, content={"detail": "Отклонено в доступе."}
    )


async def invalid_file_type_exception_handler(
    request: Request, exc: InvalidFileType
) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Неверный тип файла."},
    )


def include_exceptions_to_app(app: FastAPI):
    app.add_exception_handler(AlreadyExist, duplicate_entity_exception_handler)
    app.add_exception_handler(UserAlreadyExist, user_already_exist)
    app.add_exception_handler(NotFoundException, not_found_exception_handler)
    app.add_exception_handler(
        InvalidCredentialsException, invalid_credentials_exception_handler
    )
    app.add_exception_handler(InvalidTokenException, invalid_token_exception_handler)
    app.add_exception_handler(DatabaseException, request_processing_exception_handler)
    app.add_exception_handler(
        DatabaseConnectionException, request_processing_exception_handler
    )
    app.add_exception_handler(
        InvalidPermissionsException, invalid_permissions_exception_handler
    )
    app.add_exception_handler(InvalidFileType, invalid_file_type_exception_handler)
