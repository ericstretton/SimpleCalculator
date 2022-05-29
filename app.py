import helpers.addition as add
from helpers.addition import my_adder as add
import helpers.subtraction as sub
from helpers.subtraction import my_subtractor as sub
import helpers.multiplication as mult
from helpers.multiplication import my_multiplier as mult
import helpers.division as div
from helpers.division import my_divider as div
import helpers.welcome as greeting




greeting.welcome()

def calc():
    print("List of Operations")

    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")

    userselection = float(input(("Please select your operation('1', '2', '3', '4'): ")))

    num1 = float(input("Enter your first number here: "))
    num2 = float(input("Enter your second number here: "))

    if userselection == 1:
        print(add(num1, num2))
        
    elif userselection == 2:
        print(sub(num1, num2))
        
    elif userselection == 3:
        print(mult(num1, num2))
        
    elif userselection == 4:
        print(div(num1, num2))
            
    else:
        (userselection < 1 and userselection > 5)
        print("You have not selected an applicable operation")

calc()