rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")# end = "" ensures the symbols are printed side by side without moving to a new line after each symbol.

    print () #Moves the cursor to the next line after finishing one row. Ensures the next row starts on a new line.

    

         
