n = int(input())
g = 0
i = 0
while n>=10:    
    while True:
        g += n%10
        n = n//10
        if n == 0 :
            n = g 
            g = 0
            break
print(n)