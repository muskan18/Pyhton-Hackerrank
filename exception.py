# take input
num1, num2 = 5, 0

# Code starts here

try:
    quotient=num1%num2
    message = "Quotient is"+' '+str(quotient)
    print(message)
except ZeroDivisionError:
    message = "Cannot divide by zero"
    print(message)
# try except block
