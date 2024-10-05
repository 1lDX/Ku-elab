n = int(input())
count = 1
if n == 0:
        count = count-1  
if n == -1:
     print(count-1)
else : 
    while True:
        z = int(input()) 
        if z > n :
            count = count+1
            n += z-n
        if z == -1:
            break
    print(count)