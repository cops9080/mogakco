from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_ = list(map(int, input().split()))

for _ in range(M):
    x = int(input())
    if bisect_left(list_, x) == bisect_right(list_, x):
        print(-1)
    else:
        print(bisect_left(list_, x)+1)