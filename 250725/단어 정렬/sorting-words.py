n = int(input())
word = [input() for _ in range(n)]

sorted_word = list(sorted(word))
for elem in sorted_word:
    print(elem)