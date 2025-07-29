n = 5

class Body:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight
    def __str__(self):
        return f"{self.n} {self.h} {self.w}"

inputs = [input().split() for _ in range(n)]
people = [Body(name, height, weight) for name, height, weight in inputs]

sorted_people_name = list(sorted(people, key=lambda x: x.n))
sorted_people_height = list(sorted(people, key=lambda x: x.h, reverse=True))

print("name")
for elem in sorted_people_name:
    print(elem)

print()
print("height")
for elem in sorted_people_height:
    print(elem)