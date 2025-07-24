score = list(map(int, input().split()))

cnt_arr = [0] * 11

for elem in score:
    if elem == 0:
        break
    cnt_arr[elem//10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt_arr[i]}")
