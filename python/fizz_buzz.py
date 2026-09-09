limit = int(input("Enter the maximum number: "))
for number in range(1,limit +1):
    # Check both divisibility conditions first.
    # A number like 15 is divisible by both 3 and 5,
    # so this condition must come before the individual checks.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # If it wasn't divisible by both, check divisibility by 3.
    elif number % 3 == 0:
        print("Fizz")

    # Then check divisibility by 5.
    elif number % 5 == 0:
        print("Buzz")

    # If none of the conditions match, print the number itself.
    else:
        print(number)