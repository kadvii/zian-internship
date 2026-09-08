attempts: int = 0

while attempts < 3:
    password: str = input("Put password = ").lower()

    if password == "python123":
        attempts = attempts + 1
        print("Correct! Welcome")
        break
    else:
        attempts = attempts + 1
        print("Wrong password")

if attempts == 3:
    print("Too many attempts")