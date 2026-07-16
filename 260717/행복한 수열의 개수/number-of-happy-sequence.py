import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

happy = 0

for j in range(n):
    cnt = 1
    max_cnt = 1
    for i in range(1, n):
        if grid[i][j] == grid[i-1][j]:
            cnt += 1
        else:
            cnt = 1
    
        if max_cnt < cnt:
            max_cnt = cnt
    
    if max_cnt >= m:
        happy += 1


for i in range(n):
    cnt = 1
    max_cnt = 1
    for j in range(1, n):
        if grid[i][j] == grid[i][j-1]:
            cnt += 1
        else:
            cnt = 1
    
        if max_cnt < cnt:
            max_cnt = cnt
    
    if max_cnt >= m:
        happy += 1

print(happy)