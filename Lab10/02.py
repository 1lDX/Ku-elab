list = []
while True:
    number = int(input("Enter a number (0 to end): "))
    if number == 0:
        break
    elif number < 1 or number > 999:
        print("Number is out of range.")
    elif number >= 1 or (number >1 and number <= 999):
        list.append(number)

print("Original list:")
print(list)
print("Accumulative Sum:")
sum = 0
for i in list:
    sum = sum+i
    print(sum)