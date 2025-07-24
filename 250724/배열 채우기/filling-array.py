arr = list(map(int, input().split()))
n = len(arr)

for i in range(0, n):
    if arr[i] == 0:
        for _ in range(n-i):
            arr.pop()
        break

N = len(arr)
for i in range(N-1, -1, -1):
    print(arr[i], end=' ')