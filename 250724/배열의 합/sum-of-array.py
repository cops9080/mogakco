arr_2d = []
sum_val = 0
for _ in range(4):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for i in range(0, 4):
    sum_val = 0
    for j in range(0, 4):
        sum_val += arr_2d[i][j]
    print(sum_val)