import math
#################
hrs = int(input("Enter number of hours: "))
mins = int(input("Enter number of minutes: "))
price = 10

if hrs < 0 or mins > 59 or mins <0 :
    print("Input Error!")
elif hrs == 0 and mins <= 15 :
    print("No charge, thanks.")
elif hrs < 2 and mins >= 0 :
    price = 10
    print(f"Total amount due is {price} Bahts.")
elif hrs >= 2 and mins > 0 :
    price = (hrs+1)*10-10
    print(f"Total amount due is {price} Bahts.")
elif hrs >= 2 and mins == 0 :
    price = (price*hrs)-10
    print(f"Total amount due is {price} Bahts.")