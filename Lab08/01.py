import math
def circle(r):
    r =math.pi*r**2
    return r

def circumference(r):
    r =2*math.pi*r
    return r
def sphere(r):
    r =(4/3)*math.pi*r**3
    return r 
##
r = float(input("Enter a radius: "))
##
print('Area of a circle with radius {:.2f} is {:.2f}.'.format(r, circle(r)))
print('Circumference of a circle with radius {:.2f} is {:.2f}.'.format(r, circumference(r)))
print('Volume of sphere with radius {:.2f} is {:.2f}.'.format(r, sphere(r)))