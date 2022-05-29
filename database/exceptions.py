"""
    Database exceptions
"""


from werkzeug.exceptions import HTTPException


class DatabaseError(HTTPException):
    """ Database exception class """
    def __init__(self, code, description):
        super(DatabaseError, self).__init__(description=description)
        self.code = code


class DatabaseCompilationError(Exception):
    def __init__(self, message):
        super(DatabaseCompilationError, self).__init__(message)
