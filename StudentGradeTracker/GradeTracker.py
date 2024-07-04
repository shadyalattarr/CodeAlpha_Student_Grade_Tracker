from Student import Student
import pickle
from Grades import Grade
from Term import Term


class GPATracker:
    def __init__(self, student: Student):
        self._student = student

    def calculate_current_term_GPA(self):
        term = self._student.get_current_term()
        grades_list = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
        credit_hrs_sum = 0
        honor_points_sum = 0
        for subject, grade in term.get_subjects().items():
            print(grade)
            honor_points = grade.value * subject.get_credit_hours()
            credit_hrs_sum += subject.get_credit_hours()
            honor_points_sum += honor_points
        term_GPA = honor_points_sum / credit_hrs_sum
        self._student.get_current_term().set_term_GPA(term_GPA)
        return term_GPA

    def add_term(self, new_term: Term):
        # append term list
        self._student.append_term_list(new_term)
        for subject in new_term.get_subjects().keys():
            self._student.increment_total_credit_hrs(subject.get_credit_hours())
        # incrememnt term num
        self._student.increment_current_term_number()
        self._student.set_cgpa(self.calculate_cgpa())

    def calculate_cgpa(self):
        total_credit_hours = self._student.get_total_credit_hours()
        total_honor_points = 0
        for term in self._student.get_term_list():
            total_honor_points += term.get_term_credit_hrs()/term.get_term_GPA()
        cgpa = total_credit_hours / total_honor_points

        return cgpa

    def save_data(self):
        try:
            with open(f"{self._student.get_student_information()}.pickle", "wb") as f:
                pickle.dump(self._student, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)
