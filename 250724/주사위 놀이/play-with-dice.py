dice = list(map(int, input().split()))
cnt = 0
cnt_arr = [0] * 6

for i in range(1, 7):
    cnt = 0
    for elem in dice:
        if elem == i:
            cnt += 1
        cnt_arr[i-1] = cnt
    print(f"{i} - {cnt_arr[i-1]}")