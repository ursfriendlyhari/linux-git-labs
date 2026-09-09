rows = int(input("Enter the number of rows for the star triangle: "))

for row in range(1, rows + 1):
    # Multiplying "*" by the row number increases
    # the number of stars printed on each new line.
    print("*" * row)