def maximum(number1,number2):
    if number1 > number2:
        return number1
    else:
        return number2

number1 = float(input("please enter first number : "))
number2 = float(input("please enter second number: "))

print("maximum is", max(number1,number2))
