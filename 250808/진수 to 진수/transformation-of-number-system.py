a, b = map(int, input().split())
n = input()

binary = [int(digit) for digit in n]
num = 0

for i in range(len(binary)):
    num = num * a + binary[i]

digits = []
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num%b)
    num = num // b

for elem in digits[::-1]:
    print(elem, end='')