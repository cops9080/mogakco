n = int(input())
a = list(map(int, input().split()))

cnt = 0
min_a = min(a)
for elem in a:
    if elem == min_a:
        cnt += 1

print(f"{min_a} {cnt}")
