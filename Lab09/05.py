def fibonacci(n):
    if n <= 2:
        return 1

    fib_prev = 1
    fib_curr = 1
    i = 2

    while i < n:
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
        i += 1

    return fib_curr

##

n = int(input("Enter n: "))
print("fibo({}) = {}".format (n, fibonacci(n)))