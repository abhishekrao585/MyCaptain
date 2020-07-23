#1st task
import math as math
r=input("Enter the radius:")
R=float(r)
A=math.pi*R*R
print(A)

#2nd task
file_name=input("Input the filename:")
file_extension=file_name.split(".")
print("The extension of the file is:"+repr(file_extension[-1]))
