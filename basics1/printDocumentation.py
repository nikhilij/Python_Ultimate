"""11. Function Documentation Printer

Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument."""


def print_function_documentation():
    # Get the documentation for the built-in function 'abs'
    doc = abs.__doc__
    print("Documentation for abs():")
    print(doc)
    # You can add more built-in functions here if needed
    # For example, to print documentation for 'len':
    doc_len = len.__doc__
    print("Documentation for len():")
    print(doc_len)


if __name__ == "__main__":
    print_function_documentation()

    print(filter.__doc__)