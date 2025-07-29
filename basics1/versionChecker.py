""" 2. Python Version Checker

Write a Python program to find out what version of Python you are using. """

# sys is a module that provides access to system-specific parameters and functions.
# dir is a built-in function that returns a list of the attributes and methods of an object.

import sys
def check_python_version():
    version = sys.version
    print(f"You are using Python version: {version}")

if __name__ == "__main__":
    check_python_version()
    print("Methods and attributes in sys module:")
    print(dir(sys))