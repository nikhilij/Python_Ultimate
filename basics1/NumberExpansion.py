""" 10. Number Expansion Calculator

Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615 """

def number_expansion():
    n = int(input("Enter an integer: "))
    # Calculate the expanded value
    nn = str(n) * 2  # 'nn' is the string representation of n repeated twice
    nnn = str(n) * 3  # 'nnn' is the string representation of n repeated three times
    result = n + int(nn) + int(nnn)
    print("Expected Result:", result)

if __name__ == "__main__":
    number_expansion()