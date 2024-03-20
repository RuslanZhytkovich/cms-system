class AlreadyExist(Exception):
    pass

class UserAlreadyExist(Exception):
    pass

class NotFoundException(Exception):
    pass


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
