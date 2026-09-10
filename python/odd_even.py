"""Classify an integer as odd or even."""


def odd_even(number: int) -> str:
    """Return whether ``number`` is odd or even."""
    if number % 2 == 0:
        return f"{number} is Even"
    return f"{number} is Odd"


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(odd_even(num))
    except ValueError:
        print("Please enter a valid integer.")