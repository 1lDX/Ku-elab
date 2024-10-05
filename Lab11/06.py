vowel = "aeiou"
word = input()
i = 0
while i < len(word):
    ch = word[i]
    if ch in vowel and i + 2 < len(word) and word[i+1] == 'p' and word[i+2] == ch:
        print(ch, end="")
        i += 3
    else:
        print(ch, end="")
        i += 1