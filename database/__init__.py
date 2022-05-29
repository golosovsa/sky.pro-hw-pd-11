"""
    Database package initialization
"""


from .abstract import DatabaseMixinInterface
from .exceptions import DatabaseError, DatabaseCompilationError
from .json_database import JSONDatabase
from .meta import fabricate
