""" 32. LCM Calculator

Write a Python program to find the least common multiple (LCM) of two positive integers.
Click me to see the sample solution """

def lcm(a, b):
    """Calculate the least common multiple of two numbers."""
    def gcd(x, y):
        """Calculate the greatest common divisor using Euclidean algorithm."""
        while y:
            x, y = y, x % y
        return x
    
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    num1 = int(input("Enter first positive integer: "))
    num2 = int(input("Enter second positive integer: "))
    
    if num1 <= 0 or num2 <= 0:
        print("Both numbers must be positive integers.")
    else:
        result = lcm(num1, num2)
        print(f"The LCM of {num1} and {num2} is {result}.")