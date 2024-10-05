sp = '\\/*:|"<>." "'
word = str(input())

if "." in word :
    name,sur = word.rsplit(".",1)
    count = 0
    for i in name :
        if i in sp:
            print("_",end="")  
            count+=1
            if count >14:
                break      
        else:
            print(i,end="")
            count+=1 
            if count > 14:
                break
    print(".",end="")

    count = 0
    for i in sur :
        if i in sp:
            print("_",end="")
            count+=1
            if count >3:
                break
        else:
            print(i,end="")
            count+=1
            if count > 2 :
                break
else :
    count = 0
    for i in word :
        if i in sp:
            print("_",end="")  
            count+=1
            if count >14:
                break      
        else:
            print(i,end="")
            count+=1 
            if count > 14:
                break
    