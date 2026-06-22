import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

curr_e = 0
count = 0

for i in range(0, n):
    start_time = meetings[i][0]
    end_time = meetings[i][1]

    if start_time >= curr_e:
        count += 1
        curr_e = end_time

print(count)