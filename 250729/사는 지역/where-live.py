n = int(input())    

class Information:
    def __init__(self, name, street_address, region):
        self.name = name
        self.address = street_address
        self.region = region

inputs = [input().split() for _ in range(n)]

people = [Information(name, street_address, region) for name, street_address, region in inputs]

people = list(sorted(people, key=lambda x: x.name, reverse=True))
print(f"name {people[0].name}")
print(f"addr {people[0].address}")
print(f"city {people[0].region}")