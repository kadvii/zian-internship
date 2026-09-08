"""
أقل من 13 → Child
من 13 إلى 17 → Teenager
18 أو أكثر → Adult
"""


number = int(input("What is your age ? "))

if number < 13:
    print("Child")
elif number >=13 and number <= 17:
    print ("Teenager")
elif number >= 18:
    print("Adult")