
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

std1 = WorkingStudent('Ibrahim', 'Maseno', '250000')
std1.marks.append([89,78, 100, 76])

print(std1.marks, std1.salary)

  
    
# std1 = Student('Abdi', 'Maseno')
# std1.marks.append([89,78, 100, 76])
# # std1.marks.append(78)

# print(std1.marks)

