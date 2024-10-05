string = str(input())
word =""
for vowel in string:
    if vowel.lower() not in "aeiou":
        word+=vowel
print(word)