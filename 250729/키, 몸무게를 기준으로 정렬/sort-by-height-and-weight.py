n = int(input())

class Infor:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight
    def __str__(self):
        return f"{self.n} {self.h} {self.w}"

inputs = [input().split() for i in range(n)]
people = [Infor(name, height, int(weight)) for name, height, weight in inputs]

people = list(sorted(people, key=lambda x: (x.h, -x.w)))

for elem in people:
    print(elem)