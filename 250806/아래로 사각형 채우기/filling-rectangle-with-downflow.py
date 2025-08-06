n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for j in range(0, n):
    for i in range(0, n):
        arr[i][j] = cnt
        cnt += 1

for i in range(0, n):
    for j in range(0, n):
        print(arr[i][j], end=' ')
    print()