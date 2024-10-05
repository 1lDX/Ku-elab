print("First fraction:")
n1 = int(input(">>Enter a numerator a: "))    
d1 = int(input(">>Enter a denominator b: "))    
print("Second fraction:")
n2 = int(input(">>Enter a numerator c: "))    
d2 = int(input(">>Enter a denominator d: "))

result_num = (n1*d2 )+ (n2*d1)
print(f"Summation of the two fractions is {result_num} / {d2*d1}")