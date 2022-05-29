
def my_divider(num1, num2):
    if num2==0:
        return('function error, cannot divide by 0')
    else:
        result = num1/num2
        print("Your Result: ")
        return result

# try: 
#     result = num1/num2
# except ZeroDivisionError:
#     print("You tried to divide by 0 ")
# finally:
#     print("operation: ",num1, "/", num2, "=", result)


# try: 
#         result = num1/num2
#     except ZeroDivisionError:
#         print("You tried to divide by 0 ")
#     finally:
#         print("operation: ",num1, "/", num2, "=", result)