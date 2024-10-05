word = str(input())
list1 = []
for i in word:
    list1.append(0)

while True:
    guess = str(input())
    if guess == "0":
        break
    else :
        i = 0
        for ch in word:
            if guess == ch :
                list1[i]=1
            i+=1

i = 0
for z in list1:
    if z == 1:
        print(word[i],end='')
    else :
        print("-",end='')
    i+=1    