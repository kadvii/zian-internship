number: int = int(input("Put number = "))

if number > 10:
    print("Number must be 10 or less")
else:
    while number <= 10:
        print(number)
        number = number + 1