def palindrome(word):
    if word[::-1] == word:
        return True
    return False

while True:
    while True:
        string = input("Type a string: ").lower()

        if string:
            break
        else:
            print("Please type a string")
    
    if palindrome(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
    
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