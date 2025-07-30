n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

points = list(sorted(
    points, 
    key=lambda x: (abs(x[1][0]) + abs(x[1][1]))))

for idx, (_, _) in points:
    print(f"{idx+1}")