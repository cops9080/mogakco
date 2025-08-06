N = list(map(int, input()))
num = 0

for i in range(len(N)):
    num = num * 2 + N[i]

num = num * 17

binary = []
while True:
    if num//2 < 1:
        binary.append(num)
        break

    binary.append(num%2)
    num = num//2
    

for elem in binary[::-1]:
    print(elem, end='')