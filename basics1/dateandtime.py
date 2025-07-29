""" 3. Current DateTime Display

Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14 """

""" (method) def strftime(format: str) -> str
Format using strftime(). strftime() is a method of the datetime object that formats date and time as a string."""

from datetime import datetime
def display_current_datetime():
    now = datetime.now()
    print("Current date and time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    display_current_datetime()
    print("Methods and attributes in datetime module:")
    print(dir(datetime))