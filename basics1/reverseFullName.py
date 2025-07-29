#  write the python program to reverse a full name
"""5. Reverse Full Name

Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
Click me to see the sample solution"""


def reverse_full_name():
    fullname = input("Enter your full name :")
    # reversed_name = " ".join(fullname.split()[::-1])
    print(" ".join(fullname.split()[::-1]))

""" # Splits the input string into a list of words, reverses the list, 
    then joins it back into a string with spaces
    reversed_name = ' '.join(fullname.split()[::-1]) """

if __name__ == "__main__":
    reverse_full_name()
    


