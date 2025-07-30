#  write the python program to calculate days between two dates
""" 14. Days Between Dates

Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days """


from datetime import date

def calculate_days_between_dates():
    date1 = date(2014, 7, 2)
    date2 = date(2015, 7, 11)
    
    timedelta = date2 - date1
    days = timedelta.days
    print(f"Outupt: {days} days")

if __name__ == "__main__":
    calculate_days_between_dates()