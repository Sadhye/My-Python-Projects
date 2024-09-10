import random
import time

wins = 0
count = 0

def roll():
    nums = [1, 2, 3, 4, 5, 6]
    random_num = random.choice(nums)
    return random_num

print("DICE ROLLING PREDICTION\n")

while True:
    user = input("What will the dice roll? (1 - 6): ")
    if user.isdigit() and int(user) in range(1, 7):
        user = int(user)
    else:
        print("Please type a number between 1 to 6")
        continue

    rolled = roll()
    print("You rolled.........")
    time.sleep(2)
    print(rolled)
    time.sleep(1)

    if rolled == user:
        print(f"YES! THE NUMBER WAS {rolled}")
        wins += 1
        count += 1
    else:
        print("Oops! Better luck next time")
        count += 1
    
    while True:
        again = input("Do you want to play again? (Type yes or no): ").lower()
        if again == "yes":
            repeat = True
            break
        elif again == "no":
            print(f"You won {wins} out of {count} games")
            print("Goodbye :)")
            repeat = False
            break
        else:
            print("Please type yes or no")
    
    if repeat:
        continue
    else:
        break