word1 = input()
word2 = input()

word1 = list(sorted(word1))
word2 = list(sorted(word2))

if word1 == word2:
    print("Yes")
else: 
    print("No")
