arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

cnt_arr = [0] * cnt

for elem in arr:
    if elem > 10:
        cnt_arr[(elem//10) - 1] += 1

for i in range(0, cnt):
    print(f"{i+1} - {cnt_arr[i]}")

