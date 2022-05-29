"""
    Abstract database classes
"""


import operator
from abc import ABC


from .exceptions import DatabaseError


class DatabaseCRUDInterface(ABC):
    """ Database CRUD interface

        You must implement methods:
            .create()
            .read()
            .update()
            .delete()
    """

    def create(self):
        """ Create method of Crud interface """
        raise NotImplementedError()

    def read(self):
        """ Read method of cRud interface """
        raise NotImplementedError()

    def update(self, data):
        """ Update method of crUd interface """
        raise NotImplementedError()

    def delete(self):
        """ Delete method of cruD interface """
        raise NotImplementedError()


class DatabaseMixinInterface(DatabaseCRUDInterface, ABC):
    """ Database mixin interface

        You must implement methods:
            .is_record_valid(record)
            .is_field_valid(field, value)
    """

    # plugs for parent interface (abstract methods)

    def create(self):
        return

    def read(self):
        return list()

    def update(self, data):
        return

    def delete(self):
        return

    # interface methods

    def is_record_valid(self, record):
        """ Is this record valid? """
        raise NotImplementedError()

    def is_field_valid(self, field, value):
        """ Is this field valid? """
        raise NotImplementedError()

    # class methods

    def validate_record(self, record):
        if not self.is_record_valid(record):
            raise DatabaseError(500, f"Validate record failed ({record}).")

    def validate_field(self, field, value):
        if not self.is_field_valid(field, value):
            raise DatabaseError(500, f"Validate field failed ({field} = {value}).")

    def select_all(self):
        """ Select all records from database """
        data = self.read()
        return data

    def select_by_field(self, field, value, compare=operator.eq):
        """ Select records from database by filed """
        self.validate_field(field, value)
        data = self.read()
        result = [record for record in data if compare(record[field], value)]
        return result

    def select_one_by_field(self, field, value, compare=operator.eq):
        """ Select first record by field """
        self.validate_field(field, value)
        data = self.read()
        for record in data:
            if compare(record[field], value):
                return record
        return None

    def update_one_by_field(self, field, value, upd_record, compare=operator.eq):
        """ Update or add record by field """
        self.validate_record(upd_record)
        self.validate_field(field, value)
        data = self.read()
        for record in data:
            if compare(record[field], value):
                record.update(upd_record)
                break
        else:
            data.append(upd_record)
        self.update(data)

    def delete_one_by_field(self, field, value, compare=operator.eq):
        """ Delete record by field """
        self.validate_field(field.value)
        data = self.read()
        index = 0
        for record in data:
            if compare(record[field], value):
                break
            index += 1
        else:
            return

        del data[index]
        self.update(data)
