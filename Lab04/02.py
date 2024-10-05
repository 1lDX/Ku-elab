print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")

select = str(input("Enter your choice: "))

if select != "B" and select != "b" and select != "C" and select != "c" and select != "P" and select != "p" : 
    print("Invalid main menu choice.")

elif select == "B" or select == "b" :
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    select_menu = str(input("Enter your choice: "))
    BR = 60
    BC = 75
    BD = 90
    if select_menu != "R" and  select_menu !="r" and select_menu != "C" and select_menu != "c"and select_menu != "D" and select_menu != "d":
        print("Invalid sub menu choice.")
    
    elif select_menu == "R" or  select_menu =="r":
        print(f"Your Regular Burger is {BR} Baht.")
    elif select_menu == "C" or  select_menu =="c":
        print(f"Your Cheese Burger {BC} Baht.")
    elif select_menu == "D" or  select_menu =="d":
        print(f"Your Double Cheese Burger is {BD} Baht.")
 
elif select == "C" or select == "c":
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    select_menu = str(input("Enter your choice: "))
    CF = 120
    CG = 150
    CC = 180
    if select_menu != "F" and  select_menu !="f" and select_menu != "G" and select_menu != "g"and select_menu != "C" and select_menu != "c":
        print("Invalid sub menu choice.")
    elif select_menu == "F" or  select_menu =="f":
        print(f"Your Fried Chicken is {CF} Baht.")
    elif select_menu == "G" or  select_menu =="g":
        print(f"Your Grilled Chicken is {CG} Baht.")
    elif select_menu == "C" or  select_menu =="c":
        print(f"Your Chef's Chicken is {CC} Baht.")

elif select == "P" or select == "p":
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    select_menu = str(input("Enter your choice: "))
    PS = 90
    PL = 120
    PM = 100
    if select_menu != "S" and  select_menu !="s" and select_menu != "L" and select_menu != "l"and select_menu != "M" and select_menu != "m":
        print("Invalid sub menu choice.")
    elif select_menu == "S" or  select_menu =="s":
        print(f"Your Spaghetti de Italiano is {PS} Baht.")
    elif select_menu == "L" or  select_menu =="l":
        print(f"Your Lsagna Supreme is {PL} Baht.")
    elif select_menu == "M" or  select_menu =="m":
        print(f"Your Macaroni Special is {PM} Baht.")


    
    


        