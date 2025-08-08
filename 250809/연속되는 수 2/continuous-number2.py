n = int(input())
arr = [
    int(input()) 
    for _ in range(n)
]

max_cnt, cnt = 0, 0
for i in range(0, len(arr)):
    if i==0 or arr[i] == arr[i-1]:
        cnt += 1
    elif arr[i] != arr[i-1]:
        cnt = 1

    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)