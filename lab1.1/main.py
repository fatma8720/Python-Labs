number = int(input("Enter a number: "))
multiplication_tables = [
    [i * j for j in range(1, i + 1)] for i in range(1, number + 1)
]

print(multiplication_tables)
