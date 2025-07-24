arr = list(map(int, input().split()))

sum_val = 0
cnt = 0

for elem in arr:
    if elem < 250:
        sum_val += elem
        cnt += 1
    else:
        break

print(f"{sum_val} {sum_val/cnt:.1f}")
