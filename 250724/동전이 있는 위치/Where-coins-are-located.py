n, m = map(int, input().split())

place = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = map(int, input().split())
    place[r-1][c-1] = 1

for i in range(0, n):
    for j in range(0, n):
        print(place[i][j], end=' ')
    print()