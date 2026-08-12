#Student grade checker
print("The one, who gets top average gets a scholarship")

class Student:
    def __init__(self, name):
        self.name = name
        print(f"The student name is {name}")

    def Marks(self, Maths, science, social, telugu, english):
        self.Maths = Maths
        self.science = science
        self.social = social
        self.telugu = telugu
        self.english = english
        print(f"{self.name} scored in maths: {self.Maths}")
        print(f"{self.name} scored in science: {self.science}")
        print(f"{self.name} scored in social: {self.social}")
        print(f"{self.name} scored in telugu: {self.telugu}")
        print(f"{self.name} scored in english: {self.english}")

    def total(self):
        total_data = self.Maths + self.science + self.social + self.telugu + self.english
        print(f"{self.name}, total marks: {total_data}")
        return total_data

    def percent(self):
        percent_data = self.total() / 5
        print(f"{self.name}, percentage: {percent_data}")
        return percent_data

    def grade(self):
        p = self.percent()
        grade_data = "A" if p > 90 else ("B" if p > 60 else "C")
        print(f"{self.name}, grade: {grade_data}")
        return grade_data


L = Student("Likith")
L.Marks(100, 90, 80, 70, 60)
print(L.total())
print(L.percent())
print(L.grade())

R = Student("Renuka")
R.Marks(100, 100, 100, 100, 100)
print(R.total())
print(R.percent())
print(R.grade())

M = Student("Mythu")
M.Marks(100, 90, 80, 70, 60)
print(M.total())
print(M.percent())
print(M.grade())

students = [L, R, M]
students.sort(key=lambda s: s.percent(), reverse=True)

for rank, student in enumerate(students, 1):
    print(f"Rank {rank}: {student.name} with percent {student.percent()}")

with open("student grade.py", "a") as file:
    file.write(f"{students[0].name} got scholarship\n")