from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse

from core.exceptions import (
    DatabaseConnectionException,
    DatabaseException,
    InvalidCredentialsException,
    InvalidFileType,
    InvalidPermissionsException,
    InvalidTokenException,
    UserAlreadyExist,
    UserNotFoundException,
)


async def duplicate_entity_exception_handler(request: Request, exc: UserAlreadyExist) -> Response:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"detail": "A user with this data already exists."}
    )


async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": f"There is no user with this data: {exc}"}
    )


async def invalid_credentials_exception_handler(request: Request, exc: InvalidCredentialsException) -> Response:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Incorrect credentials."})


async def invalid_token_exception_handler(request: Request, exc: InvalidTokenException) -> Response:
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": "Invalid token."})


async def request_processing_exception_handler(
    request: Request, exc: DatabaseException | DatabaseConnectionException
) -> Response:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Please try later."})


async def invalid_permissions_exception_handler(request: Request, exc: InvalidPermissionsException) -> Response:
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": "Permission denied."})


async def invalid_file_type_exception_handler(request: Request, exc: InvalidFileType) -> Response:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Invalid file type."})


def include_exceptions_to_app(app: FastAPI):
    app.add_exception_handler(UserAlreadyExist, duplicate_entity_exception_handler)
    app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
    app.add_exception_handler(InvalidCredentialsException, invalid_credentials_exception_handler)
    app.add_exception_handler(InvalidTokenException, invalid_token_exception_handler)
    app.add_exception_handler(DatabaseException, request_processing_exception_handler)
    app.add_exception_handler(DatabaseConnectionException, request_processing_exception_handler)
    app.add_exception_handler(InvalidPermissionsException, invalid_permissions_exception_handler)
    app.add_exception_handler(InvalidFileType, invalid_file_type_exception_handler)