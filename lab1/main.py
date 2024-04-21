rows = int(input("Enter number of rows: "))
for row in range(rows):
    print(" " * (rows - row - 1) + "*" * (row + 1))
