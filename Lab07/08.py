c2 = int(input(""))
a = 1
b = 1
count = 0

while a<c2:
    b = 0
    while b<c2:
        if c2**2 == a**2+b**2 :
            count = count+1
        b=b+1

    a=a+1
    

print(count//2)
    
    