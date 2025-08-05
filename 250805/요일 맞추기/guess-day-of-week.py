m1, d1, m2, d2 = map(int, input().split())

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

elapsed_days = 0

forward = (m1, d1) < (m2, d2)

if forward:
    while (m1, d1) != (m2, d2):
        elapsed_days += 1
        d1 += 1
        if d1 > num_of_days[m1]:
            d1 = 1
            m1 += 1
else:
    while (m1, d1) != (m2, d2):
        elapsed_days -= 1
        d1 -= 1
        if d1 == 0:
            m1 -= 1
            d1 = num_of_days[m1]

print(days[elapsed_days % 7])