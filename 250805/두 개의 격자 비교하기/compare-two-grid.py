n, m = map(int, input().split())
matrix_1 = [list(map(int, input().split())) for _ in range(m)]
matrix_2 = [list(map(int, input().split())) for _ in range(m)]

checked = [[0] * n for _ in range(m)]
for i in range(0, n):
    for j in range(0, m):
        if matrix_1[i][j] == matrix_2[i][j]:
            checked[i][j] = 0
        else:
            checked[i][j] = 1

for i in range(0, n):
    for j in range(0, m):
        print(checked[i][j], end=' ')
    print()