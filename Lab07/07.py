integers = int(input("Enter positive integer: "))
R = 2
if integers > 0 :
    while R <= integers :
        while integers % R == 0 :
            print(R)
            integers //= R
        R += 1
else :
    print("Invalid number.")