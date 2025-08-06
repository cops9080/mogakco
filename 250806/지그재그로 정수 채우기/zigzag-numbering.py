n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 0
for j in range(0, m):
    if j%2 != 0:
        for i in range(n-1, -1, -1):
            arr[i][j] = cnt
            cnt += 1
    else:
        for i in range(0, n):
            arr[i][j] = cnt
            cnt += 1

for i in range(0, n):
    for j in range(0, m):
        print(arr[i][j], end=' ')
    print()

