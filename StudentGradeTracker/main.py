from Student import Student
from Subject import Subject
from Term import Term
from Grades import Grade
from GradeTracker import GPATracker
std = Student("Shadi", 8180)
subj1 = Subject("math", 3)
subj2 = Subject("math2", 3)
subj3 = Subject("math3", 3)
subj4 = Subject("math4", 3)
subj5 = Subject("math5", 3)
subj6 = Subject("math6", 3)

someterm = Term({subj1: Grade.Bplus, subj2: Grade.A_, subj3: Grade.Bplus, subj4: Grade.A_, subj5: Grade.Bplus, subj6: Grade.A})


gg = GPATracker(std)
gg.add_term(someterm)
gg.calculate_current_term_GPA()
print(someterm.get_term_GPA())
