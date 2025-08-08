a, b = map(int, input().split())
n = input()

binary = [int(digit) for digit in n]
num = 0

for i in range(len(binary)):
    num = num * a + binary[i]

digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    
    digits.append(num%2)
    num = num // 2

for elem in digits[::-1]:
    print(elem, end='')