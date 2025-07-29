""" 7. File Extension Extractor

Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java """

def get_file_extension():
    filename = input("Enter the filename: ")
    # Split the filename and get the last part after the dot
    extension = filename.split(".")[-1]
    print("File extension:", extension)

if __name__ == "__main__":
    get_file_extension()