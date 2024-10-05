h = int(input("Enter height: "))
w = int(input("Enter width: "))
i = 0
c = 0
line = 0
count = 1

if h <= 0 or w <= 0 :
    print("Invalid input, program terminates.")
else :
    while i<h:
        if i % 2 >=1:
            while c<w: 
                print(' *',end='')
                c += 1
        elif i % 2 == 0:
            while c<w:
                print('* ',end='')
                c += 1
        print()
        i += 1
        c = 0