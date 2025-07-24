score = list(map(float, input().split()))

sum_val = 0
n = len(score)

for elem in score:
    sum_val += elem

print(f"{sum_val/n:.1f}")