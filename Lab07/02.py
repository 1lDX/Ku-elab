n = int(input("Enter a number: "))
i = 0
c = 0


if n <=0 :
    print("Invalid input, program terminates.")
else:
    while i<n:
        c = 0
        while c<n-i:
            print(chr(ord("A")+c),end = "")
            c += 1
            
        print()
        i+=1