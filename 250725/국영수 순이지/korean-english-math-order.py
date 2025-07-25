n = int(input())
students = []

class Student:
    def __init__(self, name, korean, english, math):
        self.n = name
        self.kor = korean
        self.eng = english
        self.math = math
    
    def __str__(self):
        return f"{self.n} {self.kor} {self.eng} {self.math}"

for _ in range(n):
    name, korean, english, math = input().split()
    korean, english, math = int(korean), int(english), int(math)
    students.append(Student(name, korean, english, math))

students = list(sorted(students, key=lambda x: (-x.kor, -x.eng, -x.math)))

for elem in students:
    print(elem)
