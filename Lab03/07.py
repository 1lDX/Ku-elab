import math
x = float(input("Enter x : "))

result = 0
if x > 99:
    result = 2*(x**3) - x/math.sqrt(x+1)
elif x > 0 and x <=99:
    result= 3*(x**2) - (1-x)**2
elif x == 0:
    result = x  
else:
    result = math.sqrt((x**2)+1)
print(f"f({x:.2f}) = {int(math.ceil(result))}")