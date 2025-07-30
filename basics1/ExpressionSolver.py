#  write the python program to solve mathematical expressions

""" 38. Expression Solver

Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49 """


def expression_solver(x, y):
    """Calculate the expression (x + y) * (x + y)."""
    return (x + y) ** 2
if __name__ == "__main__":
    x = 4
    y = 3
    result = expression_solver(x, y)
    print(f"The result of ({x} + {y})^2 is {result}.")
