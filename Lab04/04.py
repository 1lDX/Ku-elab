buffet = str(input("Enter your buffet choice: "))

if buffet != "Korean" and buffet != "Japanese":
    print(f"Sorry, there is no {buffet} buffet.")
elif buffet == "Korean" or buffet == "Japanese":
    day = str(input("Is today Wednesday (yes/no)? "))
    if buffet == "Korean" and day == "no" :
        payment = 1500
        print(f"Your payment is {payment:.2f} Baht.")
    elif buffet == "Korean" and day == "yes":
        payment = 1500-(1500*15/100)
        print(f"Your payment is {payment:.2f} Baht.")
    elif buffet == "Japanese" and day == "no" :
        payment = 1000
        print(f"Your payment is {payment:.2f} Baht.")
    elif buffet == "Japanese" and day == "yes" :
        payment = 1000-(1000*15/100)
        print(f"Your payment is {payment:.2f} Baht.")
