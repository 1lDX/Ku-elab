payment = float(input("Enter buying amount: "))
if payment >= 1000 and payment < 3000 :
    money = payment-(payment*(10/100))
elif payment >= 3000 :
    money = payment-(payment*(15/100)) 
else :
    money = payment
print(f"Amount due after discount is {money:.2f} baht.")