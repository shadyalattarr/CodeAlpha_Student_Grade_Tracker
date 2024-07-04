class Student:

    def __init__(self, name: str, ID: int, DOB: str, term_number: int = 0):  # date?
        self._name = name
        self._ID = ID
        self._current_term_number = term_number

    def enroll_in_term(self):
        pass

    def get_term_number(self):
        return self._current_term_number

