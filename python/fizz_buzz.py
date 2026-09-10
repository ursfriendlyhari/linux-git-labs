"""Generate FizzBuzz sequences."""


def fizz_buzz(limit: int) -> list[str]:
    """Return the FizzBuzz values from 1 through ``limit``."""
    values: list[str] = []
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            values.append("FizzBuzz")
        elif number % 3 == 0:
            values.append("Fizz")
        elif number % 5 == 0:
            values.append("Buzz")
        else:
            values.append(str(number))
    return values


if __name__ == "__main__":
    limit = int(input("Enter the maximum number: "))
    print("\n".join(fizz_buzz(limit)))