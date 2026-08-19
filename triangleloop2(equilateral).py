rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to use: ")

for i in range(1, rows + 1):
    spaces = " " * (rows - i)          # leading spaces
    symbols = symbol * (2 * i - 1)     # odd number of symbols
    print(spaces + symbols)
