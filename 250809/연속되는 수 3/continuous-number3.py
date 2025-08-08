N = int(input())
arr = [
    int(input()) 
    for _ in range(N)
]

max_cnt, cnt = 0, 0
for i in range(len(arr)):
    if i==0 or arr[i] * arr[i-1] > 0:
        cnt += 1
    elif arr[i] * arr[i-1] < 0:
        cnt = 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)