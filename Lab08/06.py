import math
def sqrt_n_times(x, n):
    while n > 0:
        x = math.sqrt(x)
        n -= 1
    return x

##

x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )