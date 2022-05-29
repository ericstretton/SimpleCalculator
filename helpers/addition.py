
from multiprocessing.sharedctypes import Value


def my_adder(num1, num2):
    result = num1+num2
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Error, invalid input")
    finally:
        print("Your Result: ")
        return result
