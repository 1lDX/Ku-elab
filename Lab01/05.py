block_length = 12
block_width = 9
house_length = 7
house_width = 6

MOW_RATE = 35.0
#----------------------------------------------------------------
num1 = block_length * block_width
num2 = house_length * house_width

total = num1 - num2

cost = total * MOW_RATE
print("Mowing cost is" ,cost, "baht.")