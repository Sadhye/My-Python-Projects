while True:
    while True:
        columns = input("Enter number of columns in your rectangle: ")
        if columns.isdigit():
            columns = int(columns)
            break
        else:
            print("Input is not numeric... Try again")

    while True:
        rows = input("Enter number of rows in your rectangle: ")
        if rows.isdigit():
            rows = int(rows)
            break
        else:
            print("Input is not numeric... Try again")
            
    while True:
         symbol = input("Enter a symbol to use: ")
         if len(symbol) == 1:
            break
         else:
            print("Please type only one symbol")

    for i in range(rows):
        for j in range(columns):
            print(symbol, end="")
        print()
    
    while True:
        again = input("Do you want to make another rectangle?: ").lower()
        if again == "yes":
            break
        elif again == "no":
            print("Goodbye!")
            quit()
        else:
            print("Please type yes or no")