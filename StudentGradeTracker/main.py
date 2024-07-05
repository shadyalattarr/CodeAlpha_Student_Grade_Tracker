from Student import Student
from Subject import Subject
from Term import Term
from Grades import Grade
from GradeTracker import GPATracker
from typing import Dict
import pickle


def input_student_details() -> Student:
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    return Student(name, ID)


def add_term(gpa_tracker: GPATracker):
    gpa_tracker.add_term(create_term())


def create_term() -> Term:
    return Term(input_subjects())


def input_subjects() -> Dict[Subject, Grade]:
    number = int(input("Enter number of subjects to be registered this term: "))
    subjects = {}
    print("Enter subject name name, credit hours, and numeric grade separated by commas:\n "
          f"For example 'Math 1,3,95' would go for a subject called 'Math1' with 3 credit hours, "
          f"with a numeric grade of 95.")
    for i in range(number):
        subject = input(f"Enter subject {i + 1}: ")
        name, hrs, numeric_grade = subject.split(',')

        hrs = int(hrs)
        numeric_grade = int(numeric_grade)
        grade = get_grade(numeric_grade)
        subjects[Subject(name, hrs)] = grade
    return subjects


def get_grade(numeric_grade: int) -> Grade:
    if numeric_grade >= 97:
        return Grade.A_plus
    elif numeric_grade >= 93:
        return Grade.A
    elif numeric_grade >= 89:
        return Grade.A_minus
    elif numeric_grade >= 84:
        return Grade.B_plus
    elif numeric_grade >= 80:
        return Grade.B
    elif numeric_grade >= 76:
        return Grade.B_minus
    elif numeric_grade >= 73:
        return Grade.C_plus
    elif numeric_grade >= 70:
        return Grade.C
    elif numeric_grade >= 67:
        return Grade.C_minus
    elif numeric_grade >= 64:
        return Grade.D_plus
    elif numeric_grade >= 60:
        return Grade.D
    else:
        return Grade.F


def load_data(filename: str):
    filename_extension = f"{filename}.pickle"
    try:
        with open(filename_extension, 'rb') as inp:
            return pickle.load(inp)
    except Exception as ex:
        print("Student Not found", ex)


def old_new_student(student: Student):
    ans = input("Is this a old student? y/n: ")
    if ans == 'y':
        return GPATracker(load_data(student.get_student_information()))
    else:
        return GPATracker(student)



###---------------START---------------###
student = input_student_details()

gpa_tracker_1 = old_new_student(student)

add_term(gpa_tracker_1)
gpa_tracker_1.print_student_details()
