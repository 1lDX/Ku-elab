def digit(num):
    c1 = num%10
    return c1

def tens(num):
    c2 = (num//10) %10
    return c2

def hundreds(num):
    c3 = (num//100) %10
    return c3

def thousands(num):
    c4 = (num//1000) %10
    return c4 

def sum_digits(num):
    return  digit(num) + tens(num) + hundreds(num) + thousands(num)
###
n   = int(input('Enter a number (0 to 9999): '))
print(f'Digit place is {digit(n)}.')
print(f'Tens place is {tens(n)}.')
print(f'Hundreds place is {hundreds(n)}.')
print(f'Thousands place is {thousands(n)}.')
print(f'Sum of all digits is {sum_digits(n)}.')
