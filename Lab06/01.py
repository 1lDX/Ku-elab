target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))


outter_guess = guess
digit = 0
position_correct = 0
digit_corrent = 0
while digit < 4:
    current_target = target%10
    target = target// 10

    current_guess = outter_guess%10
    outter_guess = outter_guess// 10

    if current_target == current_guess:
        position_correct += 1
    inner = 0
    inner_digit = 0
    inner_guess = guess
    inner_origin =  0
    while inner < 4:
        inner_origin = inner_guess%10
        inner_guess = inner_guess// 10
        if current_target == inner_origin:
            digit_corrent+=1
        inner_digit += 1
        inner+= 1
    digit += 1

digit_corrent = digit_corrent - position_correct

unit = "positions"
unitd = "digits"
if position_correct == 1:
    translate = "One"
    unit = "position"
elif position_correct == 2:
    translate = "Two"
elif position_correct == 3:
    translate = "Three"
elif position_correct == 4:
    translate = "Four"
elif position_correct == 0:
    translate = "No"

if digit_corrent == 1:
    translated = "one"
    unitd = "digit"
elif digit_corrent == 2:
    translated = "two"
elif digit_corrent == 3:
    translated = "three"
elif digit_corrent == 4:
    translated = "four"
elif digit_corrent == 0:
    translated = "no"

if position_correct == 4 and digit == 4:
    print("Congratulations, you just mastered my mind!!")
else:
    print(f"{translate} {unit} correct, {translated} {unitd} correct")