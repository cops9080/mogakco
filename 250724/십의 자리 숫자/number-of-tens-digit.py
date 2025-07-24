arr = list(map(int, input().split()))

cnt_arr = [0] * 10

for elem in arr:
    if elem > 10:
        cnt_arr[(elem//10)-1] += 1

for i in range(0, 9):
    print(f"{i+1} - {cnt_arr[i]}")

