# write the python program to calculate the GCD of two numbers

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a 

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}.")