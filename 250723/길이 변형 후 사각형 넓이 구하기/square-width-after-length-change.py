k = input()

w, h = map(int, k.split())

w += 8
h *= 3

print(w)
print(h)
print(w*h)