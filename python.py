write a Python program to accept a filename from the user and print the extension of that.


filename = input("Input the Filename: ")

f_extns = filename.split(".")

print ("The extension of the file is : " + repr(f_extns[-1]))



write a Python program which accepts the radius of a circle from the user and computes area.

from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))
