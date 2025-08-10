N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

p = [0] * (N+1)
for person in student:
    p[person] += 1
    if p[person] >= K:
        print(person)
        break

if max(p) < K:
    print(-1)