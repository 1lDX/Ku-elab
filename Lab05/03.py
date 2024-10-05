odd = 0
while True :
    i =  int(input("Enter number: "))
    if i % 2 >=1 and i > 0 :
        odd = odd + 1
    if i < 0 :
        print(f'Received {odd} odd numbers')
        break