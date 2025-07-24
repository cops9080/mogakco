n, m = map(int, input().split())
cnt = 1

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(0, n):
    for j in range(0, m):
        arr_2d[i][j] = cnt
        cnt += 1
        print(arr_2d[i][j], end=' ')
    print()