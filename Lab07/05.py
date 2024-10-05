count = 0
i=0
while True:
    n = int(input("Enter a number: "))
    count = 0
    i = 0
    while i<=n :
        i=i+1
        if n%i == 0:
            count = count+1
    
    if n == 0 :
        print("End of program, goodbye.")
        break
    if n<=1:
        print("Invalid input, try again.")
    elif count == 2:
        print(f"{n} is a prime number.")
    elif count != 2:
        print(f"{n} is not a prime number.")

