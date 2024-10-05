n = int(input("Enter height: "))
k = 2
z = 3
count = 0
if n == 1 :
        print ("1")
elif n == 0:
        print("")
        
else : 
    while True:
        i = n*2-k
        print(" "*i,end="1")
        k = k+2
        if count == 0 :
             print("")
        count = count+1
        if count > 1 :
            print(" "*z,end="1\n")
            z = z+4
        if count == n:
             break