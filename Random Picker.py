import random
import time

print("RANDOM PICKER\n")

print("Don't know what to choose? Don't worry! Random Picker's got your back")
print("It picks something completely random out of some options\n")

while True:
    options = []
    while True:
        num_of_options = input("How many options do you have?: ")

        if num_of_options.isdigit():
            num_of_options = int(num_of_options)
        else:
            print("Please type in a number")
            continue

        if num_of_options >= 2:
            break
        else:
            print("There should be at least 2 options")
        
    for i in range(num_of_options):
        option = input(f"Option {i + 1}: ")
            
        options.append(option)
    
    random_option = random.choice(options)

    print("Random Picker chose.......")

    time.sleep(2)

    print(random_option)

    time.sleep(1)

    print("Now don't tell me you want to pick another option. hahaha")

    while True:
        again = input("Do you want to use random picker again?: ").lower()

        if again == "yes":
            repeat = True
            break
        elif again == "no":
            repeat = False
            break
        else:
            print("Please type yes or no")
    
    if repeat:
        continue
    else:
        print("Okay, Bye :)")
        break