word = str(input())
length= len(word)
check = []
count = 0
while True :
    guess = str(input())
    if guess == "0" :
        break
    if guess in check:
        continue

    for ch in word:
        if guess == ch :
            count += 1
    check.append(guess)
print(f"{count}/{length}")
    
    
    
