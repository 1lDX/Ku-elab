n = int(input("Enter a number: "))
i = 1
if n <= 0 :
    print("Invalid input, program terminates.")
else :
    while i <= n:
        j = 1
        while j <= i:
            print(chr(64 + j), end="")
            j += 1
        print()
        i += 1