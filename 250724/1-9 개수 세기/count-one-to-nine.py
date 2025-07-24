n = int(input())

arr = list(map(int, input().split()))

cnt = 0
for i in range(1 ,10):
    cnt = 0
    for elem in arr:
        if elem == i:
            cnt += 1
    print(cnt)