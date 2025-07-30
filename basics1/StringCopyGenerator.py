""" 20. String Copy Generator

Write a Python program that returns a string that is n (non-negative integer) copies of a given string. """

def string_copy(str, n):
    return str * n

if __name__ == "__main__":
    input_str = "Hello"
    n = 3
    result = string_copy(input_str, n)
    print("String copy result:", result)
