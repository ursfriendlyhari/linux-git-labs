#ODD EVEN number checker
def odd_even(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(odd_even(num))
    except ValueError:
        print("Please enter a valid integer.")
