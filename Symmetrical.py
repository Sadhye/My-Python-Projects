def symmetrical(string):
    if len(string) % 2 == 0:
        first_half = string[:len(string)//2]
        second_half = string[len(string)//2:]
    else:
        midpoint = len(string) // 2
        first_half = string[:midpoint]
        second_half = string[midpoint + 1:]
    
    if first_half == second_half[::-1]:
        return True
    return False

while True:
    while True:
        string = input("Type a string: ").lower()

        if string:
            break
        else:
            print("Please type a string")
    
    if symmetrical(string):
        print(f"{string} is symmetrical")
    else:
        print(f"{string} is not symmetrical")
    
    while True:
        again = input("Do you want to check another string?: ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("Okay, bye :)")
            quit()
        else:
            print("Please type yes or no")
    
    continue