class UserAlreadyExist(Exception):
    pass


class UserNotFoundException(Exception):
    def __init__(self, value):
        self.value = value


class InvalidCredentialsException(Exception):
    pass


class InvalidTokenException(Exception):
    pass


class DatabaseException(Exception):
    pass


class DatabaseConnectionException(Exception):
    pass


class InvalidPermissionsException(Exception):
    pass


class InvalidArgument(Exception):
    pass


class RequestProcessingException(Exception):
    pass


class InvalidFileType(Exception):
    pass