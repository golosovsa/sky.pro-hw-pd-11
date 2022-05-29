"""
    JSON database class
    Implementation of CRUD interface
"""

# import globals
import json
import pathlib
from filelock import FileLock, Timeout

# import locals
from .abstract import DatabaseCRUDInterface
from .exceptions import DatabaseError


class JSONDatabase(DatabaseCRUDInterface):
    """ JSON database implementation """

    # initialization and connect methods

    def __init__(self):
        self._timeout = None
        self._connection = None
        self._connection_lock = None

    def connect(self, connection, timeout=-1.0):
        path = pathlib.Path(connection).absolute()
        directory = path.parent
        name = path.name

        if not directory.exists() or not str(name).endswith(".json"):
            raise DatabaseError(500, f"Database connection failed ({connection}).")

        self._connection = str(path)
        self._connection_lock = str(path) + ".lock"
        self._timeout = timeout

    # interface methods implementation

    def create(self):
        """ Create JSON database (implemented Crud method)

        Can raise exception DatabaseError()

        :return: None
        """
        if self._connection is None:
            raise DatabaseError(500, "Create failed. Database is not connected.")

        path = pathlib.Path(self._connection)
        if path.exists():
            raise DatabaseError(500, f"Create failed. Database already exist ({self._connection}).")

        try:
            with FileLock(self._connection_lock, timeout=self._timeout):
                with open(self._connection, "xt", encoding="utf-8"):
                    pass

        except Timeout:
            raise DatabaseError(503, f"Create failed. Too many requests ({self._connection}).")
        except OSError as e:
            raise DatabaseError(500, f"Create failed. Received os error ({self._connection}).\n{e}")

    def read(self) -> list:
        """ Create JSON database (implemented cRud method)

        Can raise exception DatabaseError()

        :param self:
        :return: List of records
        """

        if self._connection is None:
            raise DatabaseError(500, "Read failed. Database is not connected.")

        path = pathlib.Path(self._connection)
        if not path.exists():
            raise DatabaseError(500, f"Read failed. Database does not exist ({self._connection}).")

        try:
            with FileLock(self._connection_lock, timeout=self._timeout):
                with open(self._connection, "rt", encoding="utf-8") as fin:
                    return json.load(fin)

        except Timeout:
            raise DatabaseError(503, f"Read failed. Too many requests ({self._connection}).")
        except json.JSONDecodeError:
            raise DatabaseError(500, f"Read failed. JSON decode error ({self._connection}).")
        except OSError as e:
            raise DatabaseError(500, f"Read failed. Received os error ({self._connection}).\n{e}")

    def update(self, data):
        """ Update JSON database (implemented crUd method)

        Can raise exception DatabaseError()

        :param data: Data to update
        :return: None
        """
        if self._connection is None:
            raise DatabaseError(500, "Update failed. Database is not connected.")

        path = pathlib.Path(self._connection)
        if not path.exists():
            raise DatabaseError(500, f"Update failed. Database does not exist ({self._connection}).")

        try:
            with FileLock(self._connection_lock, timeout=self._timeout):
                with open(self._connection, "wt", encoding="utf-8") as fou:
                    json.dump(data, fou, ensure_ascii=False)

        except Timeout:
            raise DatabaseError(503, f"Update failed. Too many requests ({self._connection}).")
        except json.JSONDecodeError:
            raise DatabaseError(500, f"Update failed. JSON decode error ({self._connection}).")
        except OSError as e:
            raise DatabaseError(500, f"Update failed. Received os error ({self._connection}).\n{e}")

    def delete(self):
        """ Delete JSON database (implemented cruD method)

        Can raise exception DatabaseError()

        :return: None
        """

        if self._connection is None:
            raise DatabaseError(500, "Delete failed. Database is not connected.")

        path = pathlib.Path(self._connection)
        if not path.exists():
            raise DatabaseError(500, f"Delete failed. Database does not exist ({self._connection}).")

        try:
            with FileLock(self._connection_lock, timeout=self._timeout):
                path = pathlib.Path(self._connection)
                path.unlink(missing_ok=True)

        except Timeout:
            raise DatabaseError(503, f"Delete failed. Too many requests ({self._connection}).")
        except OSError as e:
            raise DatabaseError(500, f"Delete failed. Received os error ({self._connection}).\n{e}")
