a, b, c = map(int, input().split())
D = 11
H = 11
M = 11

elapsed_minute = 0
while True:
    if a == 11 and (c < 11 or b < 11):
        print(-1)
        break
    if D == a and H == b and M == c:
        break
    if H >= 24:
        D += 1
        H = 0
    if M >= 60:
        H += 1
        M = 0
    M += 1
    elapsed_minute += 1

if elapsed_minute != 0:
    print(elapsed_minute)
