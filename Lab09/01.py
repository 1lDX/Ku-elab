def check_prime(n):
    div = 2 
    while div < n:
        if n % div == 0:
            return False
        div += 1
    return True
