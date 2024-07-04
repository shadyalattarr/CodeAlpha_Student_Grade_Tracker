from Student import Student
from Subject import Subject


class Term:

    def __init__(self, stud: Student, subj_list: list[Subject]):
        self._student = stud
        self._subjects = subj_list
        self._term_number = stud.get_term_number()

