def input_from_user(how_many:int):
    # this function gets input from the user, it takes one integer parameter, and it defines how many inputs the program asks. It shall return the input numbers as a list of integer
    list_of_integer = [] # start with an empty list
    for i in range(how_many):
        n = int(input("Please enter a number"))
        list_of_integer.append(n)
    return list_of_integer

def print_result(numbers:list):
    # this function displays all the numbers and the total sum
    print("Input:", numbers)
    print("Total Sum:", sum(numbers))

def main():
    inputs = input_from_user(3)
    print_result(inputs)

main()