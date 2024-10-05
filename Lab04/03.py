a = int(input("How many TVs? "))
b = int(input("How many DVD players? "))
c = int(input("How many Audio Systems? "))

result = ((a*6000)+(b*1500)+(c*3000)) 
discount = ((20/100)*result)
payment = result - discount
if result < 24000:
    print(f"Total price is {result:.02f} baht.")
    print(f"Your payment is {result:.2f} baht. Thank you!")
elif result >= 24000 :
    print(f"Total price is {result:.2f} baht.")
    print(f"You've got a discount of {discount:.2f} baht.")
    print(f"Your payment is {payment:.2f} baht. Thank you!")
