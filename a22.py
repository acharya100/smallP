rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter the sign: ")

for a in range(rows):
    for b in range(columns):
        print(symbol,end="")
    print()