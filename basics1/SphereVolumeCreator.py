# write the python program to caluclate the volume of a sphere
"""15. Sphere Volume Calculator

Write a Python program to get the volume of a sphere with radius six."""

import math


def calculateVolume(radius):
    pi = math.pi
    volume = (4 / 3) * pi * (radius**3)
    return volume

if __name__ == "__main__":
    radius = 6
    volume = calculateVolume(radius)
    print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")


