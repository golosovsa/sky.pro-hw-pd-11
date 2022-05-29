"""
    Homework №11
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/11-8d13de21a29f4467a5dd3c07217042fc

    Candidates database user queryset class
"""


from database import DatabaseMixinInterface


class Candidates(DatabaseMixinInterface):
    """ Candidates database """

    _int_fields = {"id", "age"}
    _str_fields = {"name", "picture", "position", "gender", "skills"}
    _fields = _int_fields | _str_fields

    def __init__(self):
        pass

    # interface methods implementation

    def is_record_valid(self, record):
        return all(map(self.is_field_valid, record.keys(), record.values()))

    def is_field_valid(self, field, value):

        if field not in self._fields:
            return False

        elif field in self._str_fields and type(value) is str:
            pass
        elif field in self._int_fields and type(value) is int:
            pass
        else:
            return False

        return True

    # Class methods

    def select_one_by_pk(self, pk):
        """ Select records by id """
        result = self.select_one_by_field("id", pk)
        return result

    def select_by_skill(self, skill):
        """ Select records by skill """
        def compare_skill(kit, desired):
            kit = set(kit.strip().lower().split(", "))
            desired = desired.strip().lower()
            return desired in kit

        return self.select_by_field("skills", skill, compare=compare_skill)

    def select_by_name(self, name):
        """ Select records by name """
        def compare_name(full, desired):
            return desired.strip().lower() in full.lower()

        return self.select_by_field("name", name, compare=compare_name)

    def select_skills(self):
        data = self.select_all()
        skills = set()
        for record in data:
            skills |= set(record["skills"].strip().lower().split(", "))
        return skills
