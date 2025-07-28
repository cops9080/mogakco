class Student:
    def __init__(self, height, weight, number):
        self.h = height
        self.w = weight
        self.n = number
    def __str__(self):
        return f"{self.h} {self.w} {self.n}"

n = int(input())
students = []

for i in range(n):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i + 1))

students = list(sorted(students, key=lambda x: (-x.h, -x.w, x.n)))

for elem in students:
    print(elem)