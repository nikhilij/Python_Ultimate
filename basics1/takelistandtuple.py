""" 6. List and Tuple Generator

Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23') """

def generate_list_and_tuple():
    input_sequence = input("Enter a sequence of comma-separated numbers: ")
    number_list = input_sequence.split(",")
    number_tuple = tuple(number_list)

    print("List:", number_list)
    print("Tuple:", number_tuple)  

if __name__ == "__main__":
    generate_list_and_tuple()