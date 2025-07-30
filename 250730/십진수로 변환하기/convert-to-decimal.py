binary = list(input())

num = 0
for i in range(0, len(binary)):
    num = num * 2 + int(binary[i])

print(num)