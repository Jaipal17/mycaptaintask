#Radius and Area of circle

from math import pi
r=float(input("Input the radius of the circle : "))
area=pi*r*r
print("The area of the circle with radius 1.1 is:",area)

#Filename and Extension

fn=input("Input the Filename: ")
f=fn.split(".")
print("The extension of the file is : "+repr(f[-1]+"thon"))

