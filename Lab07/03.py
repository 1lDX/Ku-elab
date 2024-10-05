n = int(input("Enter a number: "))
i = 0
c = 0


if n <=0 or n > 26 :
    print("Invalid input, program terminates.")
else:
    while i<n:
        c = 0
        while c<=i:
            print(chr(ord("A")+c),end = "")
            c += 1
        print()
        i+=1   

    i = 0
    c = 0
    while i<n:
        c = 0
        while c<n-i-1:
            print(chr(ord("A")+c),end = "")
            c += 1
            
        print()
        i+=1