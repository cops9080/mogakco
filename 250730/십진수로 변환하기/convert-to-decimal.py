binary = list(input())

num = 0
for i in range(0, 5):
    num = num * 2 + int(binary[i])

print(num)