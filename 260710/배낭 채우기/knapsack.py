# N: 보석의 개수, M: 배낭의 최대 용량
N, M = map(int, input().split())

values = [-1]
weights = [-1]

for _ in range(N):
    w, v = map(int, input().split())
    values.append(v)
    weights.append(w)

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for w in range(1, M+1):
        weight_i = weights[i]
        value_i = values[i]

        if weight_i > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], value_i + dp[i-1][w - weight_i])

print(dp[N][M])
