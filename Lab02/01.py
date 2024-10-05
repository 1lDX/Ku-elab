import math

r = int(input("Enter a radius: "))
area = math.pi * (r**2)
carea = 2*math.pi*r
print("Area of a circle with radius" ,r,"is","%.2f"%area,)
print("Circumference of a circle with radius",r,"is","%.2f"%carea,)