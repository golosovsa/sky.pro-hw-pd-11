"""
    Database metaclass
"""

from .abstract import DatabaseCRUDInterface, DatabaseMixinInterface
from .exceptions import DatabaseCompilationError


# class Database(type):
#     """ Metaclass for database fabrication """
#     def __init__(cls, name, bases, dct):
#         if len(bases) < 2:
#             raise DatabaseCompilationError("The database should consist of at least two classes\n"
#                                            "The first class should be inherited from DatabaseCRUDInterface.\n"
#                                            "The second class should be inherited from DatabaseMixinInterface")
#
#         if super(bases[0]) is not DatabaseCRUDInterface:
#             raise DatabaseCompilationError("The first class should be inherited from DatabaseCRUDInterface.")
#
#         if super(bases[1]) is not DatabaseMixinInterface:
#             raise DatabaseCompilationError("The second class should be inherited from DatabaseMixinInterface")
#
#         return super(Database, cls).__init__(name, bases, dct)

# @staticmethod
def fabricate(name, class_crud: type, class_mixin: type) -> type:
    """ Fabricate a new database class

    Can raise exception DatabaseCompilationError

    :param name: Name of new class
    :param class_crud: Implemented CRUD interface for database
    :param class_mixin: Implemented user interface for Database
    :return: New class (not instance)
    """

    if DatabaseCRUDInterface not in class_crud.__mro__:
        raise DatabaseCompilationError("The first class should be inherited from DatabaseCRUDInterface.")
    if DatabaseMixinInterface not in class_mixin.__mro__:
        raise DatabaseCompilationError("The second class should be inherited from DatabaseMixinInterface")
    return type(name, (class_crud, class_mixin), {})


