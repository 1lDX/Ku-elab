age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))

if age <15 or age>60 :
    print("Invalid age.")
elif income < 1 or income > 79999 :
    print("Invalid income.")


elif income >= 1 and income <= 30000 :
    income = (income*(20/100))
    print(f"Your negative income tax is {income:.2f} Baht.")

elif income > 30000 and income <=79999 :
    income = (30000*20/100)-((income-30000)*12/100) 
    print(f"Your negative income tax is {income:.2f} Baht.")
