rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to use: ")

for i in range(1, rows + 1):   # start from 1 up to rows
    for j in range(i):         # print 'i' symbols in each row
        print(symbol, end="")
    print()                    # move to next line
