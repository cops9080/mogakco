n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

c = 0
cnt = 1
R = m+n-1
for t in range(R):
    for i in range(t + 1):
        j = t - i
        if 0 <= i < n and 0 <= j < m:
            arr[i][j] = cnt
            cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

# 0,0 t=0 / i=0 / j=0 

# t=1
# 0,1 i=0 / j=1 / j=t-i
# 1,0 i=1 / j=0 / j=t-i

# t=2
# 0,2 i=0 / j=2
# 1,1 i=1 / j=1
# 2,0 i=2 / j=0

# 0,3
# 1,2
# 2,1
# 3,0

# 0,4
# 1,3
# 2,2
# 3,1
# 4,0

# i = n - j