word = str(input())
sp = "- _ = . $"
i = 0
for ch in word:
    if ch in sp:
        i+=1
        continue
    else :
        if word[i-1] in sp:
            if i == 1:
                print(ch.lower(),end="")
            else:
                print(ch.upper(),end="")
        else:
            print(ch.lower(),end="")
    i+=1