n, m = map(int, input().split())

move_A = [tuple(input().split()) for _ in range(n)]
move_B = [tuple(input().split()) for _ in range(m)]

dir_a = [0] * 20
dir_b = [0] * 20

# move A
pos = 0
time_idx = 0
for d, t in move_A:
    t = int(t)
    step = -1 if d == "L" else 1
    for _ in range(t):
        pos += step
        dir_a[time_idx] = pos
        time_idx += 1

# move B
pos = 0
time_idx = 0
for d, t in move_B:
    t = int(t)
    step = -1 if d == "L" else 1
    for _ in range(t):
        pos += step
        dir_b[time_idx] = pos
        time_idx += 1

meet_time = -1
for i in range(min(len(dir_a), len(dir_b))):
    if dir_a[i] == dir_b[i]:
        meet_time = i + 1
        break

print(meet_time)
