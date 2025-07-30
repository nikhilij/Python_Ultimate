# wap to check whether the given number is even or odd

def check(num):
    if num %2 ==0:
        return "Even"
    else:
        return "Odd"
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check(num)
    print(f"The number {num} is {result}.")    