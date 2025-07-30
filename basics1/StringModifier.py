""" 19. Prefix "Is" String Modifier

Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is". """

def addprefix_is(str):
    if str.startswith("Is"):
        return str
    else:
        return "Is" + str
    
if __name__ == "__main__":
    input_str = "IsShowSpeed"
    another_str = "ShowSpeed"
    result = addprefix_is(input_str)
    print("Modified string:", result)
    print(addprefix_is(another_str))