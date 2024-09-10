while True:
    while True:
        calculation = input("Enter a calculation or type 'quit()' to quit: ")
        try:
            result = eval(calculation)
            break
        except ZeroDivisionError:
            print("Can't divide by 0")
            continue
        except:
            print("Invalid expression")

    print(f"{calculation} = {result}")