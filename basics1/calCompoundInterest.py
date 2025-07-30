""" 39. Future Value Calculator

Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79 """

def calc(principal,rate,years):
    """Calculate the future value of a principal amount."""
    return principal * ((1 + rate / 100) ** years)

if __name__ == "__main__":
    amt = 10000
    int_rate = 3.5
    years = 7
    future_value = calc(amt, int_rate, years)
    print(f"Future Value: {future_value:.2f}")
