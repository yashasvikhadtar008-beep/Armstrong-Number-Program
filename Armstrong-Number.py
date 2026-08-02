# Armstrong Number Checker

def is_armstrong(num):
    digits = str(num)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == num


# Main Program
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number")