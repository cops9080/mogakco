import sys
input = lambda:sys.stdin.readline().rstrip()

A = input()
B = input()
N = len(A)
M = len(B)

dp = [[0] * (M+1) for _ in range(N+1)]

max_len = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if max_len < dp[i][j]:
                max_len = dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max_len)