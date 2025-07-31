n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = [0] * 200

for x1, x2 in segments:
    if x1 * x2 < 0 and x1 < x2:
        x1 = 0
        x2 = x2 + abs(x1)
    elif x1 * x2 < 0 and x1 > x2:
        x2 = 0
        x1 = x1 + abs(x2)
    for i in range(x1, x2):
        line[i] += 1

max_line = max(line)
print(max_line)