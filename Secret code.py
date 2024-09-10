def secret_code(string):
    new_string = ""
    for i in string.lower():
        if i == "a":
            new_string = f"{new_string} 1"
        if i == "b":
            new_string = f"{new_string} 2"
        if i == "c":
            new_string = f"{new_string} 3"
        if i == "d":
            new_string = f"{new_string} 4"
        if i == "e":
            new_string = f"{new_string} 5"
        if i == "f":
            new_string = f"{new_string} 6"
        if i == "g":
            new_string = f"{new_string} 7"
        if i == "h":
            new_string = f"{new_string} 8"
        if i == "i":
            new_string = f"{new_string} 9"
        if i == "j":
            new_string = f"{new_string} 10"
        if i == "k":
            new_string = f"{new_string} 11"
        if i == "l":
            new_string = f"{new_string} 12"
        if i == "m":
            new_string = f"{new_string} 13"
        if i == "n":
            new_string = f"{new_string} 14"
        if i == "o":
            new_string = f"{new_string} 15"
        if i == "p":
            new_string = f"{new_string} 16"
        if i == "q":
            new_string = f"{new_string} 17"
        if i == "r":
            new_string = f"{new_string} 18"
        if i == "s":
            new_string = f"{new_string} 19"
        if i == "t":
            new_string = f"{new_string} 20"
        if i == "u":
            new_string = f"{new_string} 21"
        if i == "v":
            new_string = f"{new_string} 22"
        if i == "w":
            new_string = f"{new_string} 23"
        if i == "x":
            new_string = f"{new_string} 24"
        if i == "y":
            new_string = f"{new_string} 25"
        if i == "z":
            new_string = f"{new_string} 26"
    
    print(new_string)

while True:
    s = input("Enter a string: ")
    if len(s) == 0:
        print("Please type in a string")
        continue
    else:
        print(f"'{s}' in secret code is:")
        secret_code(s)
    while True:
        again = input("Do you want to convert another string? (Type yes or no): ").lower()
        if again == "yes":
            repeat = True
            break
        elif again == "no":
            print("Okay, bye :)")
            repeat = False
            break
        else:
            print("Please type yes or no")
    
    if repeat:
        continue
    else:
        break