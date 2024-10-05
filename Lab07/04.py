n = int(input("Enter a number: "))
sett = 0
x = 0
char = ""
if n >= 0 :
    while sett <= n :
        fac = n - (n - sett)
        if fac == 0 :
            print(f"{fac}! = 1 = 1")
        else :
            while fac <= n :
                result = 1
                infac = fac
                char = f"{fac}! ="
                while infac > 0 :
                    char += f" {infac}"
                    result *= infac
                    infac -= 1
                    if infac > 0:
                        char += " x" 
                char += f" = {result}"
                print(char)
                break
        sett += 1
else :
    print("Invalid input, program terminates.") 