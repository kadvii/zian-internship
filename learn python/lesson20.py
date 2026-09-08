try:
    number1 = int(input("Enter First number: "))
    number2 = int(input("Enter Second number: "))

    number3 = number1 / number2

    print(number3)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")