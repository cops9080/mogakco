k = input()

m, l = map(int, k.split())

if m>=90:
    if l>=95:
        print("100000")
    elif l>=90 and l<95:
        print("50000")
    else:
        print("0")
else:
    print("0")