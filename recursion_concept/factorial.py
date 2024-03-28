#!/bin/python3


def factorial(nr):

    #base condition
    if nr == 1:
        return 1
    #recursive iteration until the function reaches the base condition
    else:
        return (nr * factorial(nr -1))
    


if __name__ == "__main__":

    

    while True:
        try:
            userInput = int(input("Please type a number to calculate the factorial:"))
            if userInput == -1:
                break
            else:
                print(factorial(userInput))
        except ValueError:
            print("That's not a valid number. Please try again.")
