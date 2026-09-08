numbers = [12, 7, 25, 4, 18, 9, 30]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
        even_count = even_count + 1
    else:
        print(f"{number} is odd")
        odd_count = odd_count + 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")