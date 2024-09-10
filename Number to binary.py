while True:
    while True:
        num = input("Type a number: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Please type a number")
    
    print(num, "in binary is", bin(num)[2:])
    
    while True:
        again = input("Do you want to convert another number?: ").lower()
        if again == "no":
            print("Okay, Bye!")
            quit()
        elif again == "yes":
            break
        else:
            print("Please type yes or no")