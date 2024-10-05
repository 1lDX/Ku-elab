target = 72
count = 0
while True:
    n = int(input("Enter your guess: "))
    count = count+1
    if n < 0 or n > 100 :
        print("Sorry, your guess is out of range.")
    elif n < target :
        print("Sorry, your guess is too low.")
    elif n > target :
        print("Sorry, your guess is too high.")
    elif n == target :
        print(f"Congratulations, your guess is correct.") 
        break
print(f"Total number of guesses is {count}.")    