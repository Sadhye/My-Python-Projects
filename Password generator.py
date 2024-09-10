import random

def password_generator():
    characters = ["Q", "q", "W", "w", "E", "e", "R", "r", "T", "t", "Y", "y", "U", "u", "I", "i", "O", "o", "P", "p", "A", "a", "S", "s", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "Z", "z", "X", "x", "C", "c", "V", "v", "B", "b", "1", "!", "2", "@", "3", "#", "4", "$", "5", "%", "6", "^", "7", "&", "8", "*", "9", "(", "0", ")", "[", "]", "{", "}", ":", ";", ",", "<", ".", ">", "/", "?", "+", "=", "-", "_", "~", "`"]
    while True:
        length = input("Enter the length of your password: ")
        if length.isdigit():
            length = int(length)
            break
        else:
            print("Input is not numeric... Try again")
    
    print("Your password is:")
    for i in range(length):
        print(random.choice(characters), end="")
    print()

password_generator()