class NoEntityByIdFound(Exception):
    pass


class IncorrectTokenStructure(Exception):
    pass


class IncorrectTokenContent(Exception):
    pass


class InvalidSignature(Exception):
    pass


class ExpiredTokenError(Exception):
    pass
