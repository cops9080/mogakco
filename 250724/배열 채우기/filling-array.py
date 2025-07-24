arr = list(map(int, input().split()))
n = len(arr)

for i in range(n-1, -1, -1):
    if arr[i] != 0:
        print(arr[i], end=' ')