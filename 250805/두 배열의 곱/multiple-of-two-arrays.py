matrix_1 = [list(map(int, input().split())) for _ in range(3)]
blank = input()
matrix_2 = [list(map(int, input().split())) for _ in range(3)]

result = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(0, 3):
    for j in range(0, 3):
        result[i][j] = matrix_1[i][j] * matrix_2[i][j]

for i in range(0, 3):
    for j in range(0, 3):
        print(result[i][j], end=' ')
    print()