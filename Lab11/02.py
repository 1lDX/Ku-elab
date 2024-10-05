word  = str(input())
count = 0
for vowel in word:
    if (vowel == "a" or vowel == "A") or (vowel == "e" or vowel == "E") or (vowel == "i" or vowel == "I") or (vowel == "o" or vowel == "O") or (vowel == "u" or vowel == "U") :
        count += 1
print(count)