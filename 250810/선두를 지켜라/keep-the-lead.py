n, m = map(int, input().split())

# Process A's movements
moveA = [
    tuple(map(int, input().split())) for _ in range(n)
]

posA = []
for v, t in moveA:
    for _ in range(t):
        posA.append(posA[-1] + v if posA else v)

# Process B's movements
moveB = [
    tuple(map(int, input().split())) for _ in range(m)
]

posB = []
for v, t in moveB:
    for _ in range(t):
        posB.append(posB[-1] + v if posB else v)

# s = vt

cnt = 0
prev_leader = 0

for i in range(len(posA)):
    if posA[i] > posB[i]:
        current_leader = 1
    elif posA[i] < posB[i]:
        current_leader = 2
    else:
        current_leader = 0
    
    if i > 0 and current_leader != prev_leader and current_leader != 0:
        cnt += 1

    prev_leader = current_leader

print(cnt)