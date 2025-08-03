N, B = map(int, input().split())

binary = [] * 1000

while True:
    if B == 4:
        if N < 4:
            binary.append(N)
            break    
        binary.append(N % 4)
        N //= 4
    if B == 8:
        if N < 8:
            binary.append(N)
            break    
        binary.append(N % 8)
        N //= 8
for num in binary[::-1]:
    print(num, end='')
