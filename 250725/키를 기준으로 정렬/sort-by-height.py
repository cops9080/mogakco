class Student:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight
    
    def __str__(self):
        return f"{self.n} {self.h} {self.w}"

n = int(input())
students = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    h_i, w_i = int(h_i), int(w_i) 
    students.append(Student(n_i, h_i, w_i))

students = list(sorted(students, key=lambda x: x.h))

for elem in students:
    print(elem)