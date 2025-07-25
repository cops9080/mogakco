n = int(input())
students = []

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def __str__(self):
        return f"{self.name} {self.kor} {self.eng} {self.math}"

for _ in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    students.append(Student(name, kor, eng, math))

students = list(sorted(students, key=lambda x: (x.kor + x.eng + x.math)))

for elem in students:
    print(elem)