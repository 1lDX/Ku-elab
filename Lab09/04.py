def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        i = 1
        while i <= n:
           result *= i
           i += 1
        return result
##
n = int(input("Enter n: "))
print(f'{n}!', "=", factorial(n))