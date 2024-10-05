target = 72
##########
Guess = int(input("Enter your guess (0 - 100): "))
if Guess < 0 or Guess > 100 :
    print("Sorry, out of range, try again later.")
elif target == Guess :
    print("Congratulations, your guess is correct.")
else :
    print("Sorry, your guess is wrong, try again later.")