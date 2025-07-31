n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = [0] * 200
min_point = min(segments)[0]

for x1, x2 in segments:
    x1 += abs(min_point)
    x2 += abs(min_point)
    for i in range(x1, x2):
        line[i] += 1

max_line = max(line)
print(max_line)