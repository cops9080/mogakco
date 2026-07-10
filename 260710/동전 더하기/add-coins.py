import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coin = []

for _ in range(N):
    c = int(input())
    coin.append(c)

ans = 0
for c in coin[::-1]:
    ans += M // c
    M %= c
    if M == 0:
        break

print(ans)