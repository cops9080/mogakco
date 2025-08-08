nA, mB = map(int, input().split())

dA = []
tA = []
for _ in range(nA):
    direction, time = input().split()
    dA.append(direction)
    tA.append(int(time))

dB = []
tB = []
for _ in range(mB):
    direction, time = input().split()
    dB.append(direction)
    tB.append(int(time))

# Please write your code here.
dir_a = [0] * nA
dir_b = [0] * mB

# A move
for i in range(0, nA):
    if i == 0:
        if dA[i] == "L":
            dir_a[i] = -tA[i]
        elif dA[i] == "R":
            dir_a[i] = tA[i]
    else:
        if dA[i] == "L":
            dir_a[i] = dir_a[i-1] - tA[i]
        elif dA[i] == "R":
            dir_a[i] = dir_a[i-1] + tA[i]

# B move
for i in range(0, mB):
    if i == 0:
        if dB[i] == "L":
            dir_b[i] = -tB[i]
        elif dB[i] == "R":
            dir_b[i] = tB[i]
    else:
        if dB[i] == "L":
            dir_b[i] = dir_b[i-1] - tB[i]
        elif dB[i] == "R":
            dir_b[i] = dir_b[i-1] + tB[i]

cnt = 0
for i in range(0, len(dir_a)):
    for j in range(0, len(dir_b)):
        cnt += 1
        if dir_a[i] == dir_b[j]:
            break

print(cnt)