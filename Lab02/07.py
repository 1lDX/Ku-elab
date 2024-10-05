import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a1 = f"{math.pow(x,y) + z:.2f}"
a2 = f"{math.cos(math.pi*2) + math.log(x):.2f}"
a3 = f"{abs(x) + abs(y):.2f}"
a4 = f"{math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2)):.2f}"
a5 = f"{math.pow(math.sin(x),2) + math.pow(math.cos(x),2):.2f}"
a6 = f"{round((x+y)**(1/5), 6):.2f}"
a7 = f"{math.e**(x*math.log(y)):.2f}"

print(f"a1 = {a1}")
print(f"a2 = {a2}")
print(f"a3 = {a3}")
print(f"a4 = {a4}")
print(f"a5 = {a5}")
print(f"a6 = {a6}")
print(f"a7 = {a7}")