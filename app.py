from addition import my_adder as ADD
from subtraction import my_subtractor as SUB
from multiplication import my_multiplier as MULT
from division import my_divider as DIV

# import addition
# import subtraction
# import multiplication
# import division

print("Select Operation")

print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")
print("Please enter your selection: ")

userselection = input("Enter Selection( '1', '2', '3', '4'): ")

print("Please enter your first number: ")
num1 = float(input("Selection: "))

print("Please enter your second number: ")
num2 = float(input("your selection here: "))

if userselection == "1":
    # print(addition.my_adder(num1, num2))
    print(ADD)
elif userselection == "2":
    # print(subtraction.my_subtractor(num1, num2))
    print(SUB)
elif userselection == "3":
    # print(multiplication.my_multiplier(num1, num2))
    print(MULT)
elif userselection == "4":
    # print(division.my_divider(num1, num2))
        print(DIV)

print("Your Result: ")
