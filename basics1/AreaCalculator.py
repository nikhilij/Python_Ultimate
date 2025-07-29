""" 4. Circle Area Calculator

Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504 """

import math

def calculatearea(radius):
    area = math.pi * (radius ** 2)
    return area

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        area = calculatearea(radius)
        print(f"Area of the circle with radius {radius} is: {area}")
    except ValueError as e:
        print(f"Invalid input: {e}")

