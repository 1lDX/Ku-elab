word = str(input())
vowel = "aeiouAEIOU"

for ch in word :
    if ch not in vowel :
        print(ch.lower(),end="")
    else :
        print(ch.upper(),end="")