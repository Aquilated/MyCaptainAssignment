# Created by Rachit Master.

# Task 1 - Area of a circle

"""
value of pi was set.
once you input the radius of the circle, it will use the area of a circle formula which is 'pi * r * r'.
the result is then printed.
"""

pi = 3.141592653589793238
radius = float(input("Input the radius of the Circle: "))
area = pi * radius * radius
print("The area of the circle with radius", radius, "is: ", area)


# Task 2 - Extension of a file name

"""
after taking the input of you file, it will split the file into 2 from the "." and then it will print the
2nd function.
"""

file = input("Input the Filename: ")
extension = file.split(".")
print("The extension of the file is: ", extension[1])
