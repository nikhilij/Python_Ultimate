""" 12. Monthly Calendar Display

Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module. """

import calendar
def display_monthly_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()
    
    # Display the calendar for the specified month and year
    print(cal.formatmonth(year, month))

if __name__ == "__main__":
    display_monthly_calendar()