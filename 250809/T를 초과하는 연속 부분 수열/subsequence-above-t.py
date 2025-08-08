n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_cnt, cnt = 0, 0
for val in arr:
    if val > t:
        cnt += 1    
    else:
        cnt = 0
    max_cnt = max(max_cnt, cnt)

print(max_cnt)