import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [-1, 1, -1, 1, -1, 1, 0, 0]
dys = [0, 0, 1, -1, -1, 1, -1, 1]

curr_max = float('-inf')
curr = 0
for y in range(n):
    for x in range(n):

        curr = grid[y][x]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                curr = float('-inf')
                continue
            curr += grid[ny][nx]
        if curr == float('-inf'):
            curr = 0
            continue
        elif curr_max < curr:
            curr_max = curr
            curr = 0

print(curr_max)