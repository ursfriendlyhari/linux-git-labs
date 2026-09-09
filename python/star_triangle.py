rows = int(input("Enter how many rows "))

for row in range(1, rows + 1):
    # Multiplying "*" by the row number increases
    # the number of stars printed on each new line.
    print("*" * row)