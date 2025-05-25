#Calculator

Operator = input("Enter The Operator(+,-,*,/):")
num1 = int(input("Enter a number 1:"))
num2 = int(input("Enter a number 2:"))


if Operator == "+":
    result=(num1 + num2)
    print(result)

elif Operator == "-":
    result=(num1 - num2)
    print(result)

elif Operator == "*":
    result=(num1 * num2)
    print(result)

elif Operator == "/":
    result=(num1 / num2)
    print(result)
