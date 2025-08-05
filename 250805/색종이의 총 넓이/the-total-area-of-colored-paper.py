OFFSET = 100

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

paper = [[0] * 200 for _ in range(200)]

for i in range(0, n):
    x1, y1 = points[i]
    x1, y1 = x1 + OFFSET, y1 + OFFSET

    for x in range(x1, x1 + 8):
        for y in range(y1, y1 + 8):
            paper[x][y] += 1

area = 0
for i in range(0, 200):
    for j in range(0, 200):
        if paper[i][j] != 0:
            area += 1

print(area)