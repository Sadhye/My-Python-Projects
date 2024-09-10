from random import randint

print("Welcome to the number guessing game!\n")

print("Here are the rules:")
print("1. You will choose a range between two numbers")
print("2. The computer will choose a random number between that range")
print("3. You have to guess what the number is. If the number you guessed was lower than the actual number, it will respond 'Too low!', if it is higher, it will respond 'Too high!'\n")

while True:
    tries = 0

    while True:
        num1 = input("Enter the first number of the range: ")

        if num1.isdigit():
            num1 = int(num1)
            print()
            break
        else:
            print("Please type a positive integer")
    
    while True:
        num2 = input("Enter the second number of the range: ")

        if num2.isdigit():
            num2 = int(num2)
        else:
            print("Please type a positive integer")
            continue

        if num2 <= num1:
            print(f"The number has to be bigger than the first number ({num1})")
        else:
            print()
            break
    
    random_num = randint(num1, num2)
    print(f"The computer has chose a random number between {num1} and {num2}\n")

    while True:
        guess = input(f"Guess a number between {num1} and {num2}: ")

        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please type a positive integer\n")
            continue

        if guess not in range(num1, num2 + 1):
            print(f"Please type a number between {num1} and {num2}\n")
            continue

        if guess < random_num:
            print("Too low!\n")
            tries += 1
            continue
        if guess > random_num:
            print("Too high!\n")
            tries += 1
            continue
        if guess == random_num:
            print(f"YES! THE NUMBER WAS {random_num}!")
            print()
            tries += 1
            break
    
    print(f"It took you {tries} tries to guess the number\n")

    while True:
        again = input("Do you want to play again?: ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("Okay, bye :)")
            quit()
        else:
            print("Please type yes or no\n")
    
    continue