def alternating(n):
    i = 1
    result = 0
    while i <= n:
        if i %2 == 0:
            result -= i
        else:
            result+=i
        i+=1
    return result

##

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,alternating(n)))