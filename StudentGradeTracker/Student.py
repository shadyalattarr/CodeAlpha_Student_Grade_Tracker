from Subject import Subject
from typing import Dict
from Grades import Grade
from Term import Term


class Student:

    def __init__(self, name: str, ID: int):  # date?
        self._name = name
        self._ID = ID
        self._CGPA = 4.0
        self._total_credit_hrs = 0
        self._current_term_number = -1
        self._term_list = []

    def get_CGPA(self):
        return self._CGPA

    def get_term_list(self):
        return self._term_list

    def get_total_credit_hours(self):
        return self._total_credit_hrs

    def append_term_list(self, term: Term):
        self._term_list.append(term)

    def increment_total_credit_hrs(self, hours):
        self._total_credit_hrs += hours

    def increment_current_term_number(self):
        self._current_term_number += 1

    def set_cgpa(self, cgpa: float):
        self._CGPA = cgpa

    def get_current_term(self) -> Term:
        return self._term_list[self._current_term_number]

    def get_term_number(self):
        return self._current_term_number

    def get_student_information(self):
        return f"{self._name}_{self._ID}"

    def __repr__(self):
        return f"Student: {self._name} - {self._ID}"
