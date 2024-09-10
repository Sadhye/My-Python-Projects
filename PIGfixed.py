import random

def roll():
    random_num = random.randint(1, 6)
    return random_num

player1_points = player2_points = player3_points = player4_points = player5_points = player6_points = 0
TARGET_SCORE = 100

while True:
    players = input("How many players are playing (2 - 5): ")
    if players.isdigit():
        players = int(players)
    else:
        print("Please type in a number between 2 to 5")
        continue

    if players in range(2, 6):
        break
    else:
        print("Number not in range... Try again")

print(f"Target score: {TARGET_SCORE}")

if players == 2:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    print(f"Hello {player1} and {player2}!")

    while True:
        print(f"{player1}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player1_points >= TARGET_SCORE:
                print(f"{player1.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player1_points += current_points
                        print(f"Total points of {player1} are: {player1_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player1_points += current_points
                print(f"Total points of {player1} are: {player1_points}")
                break
    
        print(f"{player2}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player2_points >= TARGET_SCORE:
                print(f"{player2.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player2_points += current_points
                        print(f"Total points of {player2} are: {player2_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player2_points += current_points
                print(f"Total points of {player2} are: {player2_points}")
                break

if players == 3:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")

    print(f"Hello {player1}, {player2} and {player3}!")

    while True:
        print(f"{player1}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player1_points >= TARGET_SCORE:
                print(f"{player1.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player1_points += current_points
                        print(f"Total points of {player1} are: {player1_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player1_points += current_points
                print(f"Total points of {player1} are: {player1_points}")
                break
    
        print(f"{player2}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player2_points >= TARGET_SCORE:
                print(f"{player2.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player2_points += current_points
                        print(f"Total points of {player2} are: {player2_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player2_points += current_points
                print(f"Total points of {player2} are: {player2_points}")
                break
        
        print(f"{player3}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player3_points >= TARGET_SCORE:
                print(f"{player3.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player1_points += current_points
                        print(f"Total points of {player3} are: {player3_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player3_points += current_points
                print(f"Total points of {player3} are: {player3_points}")
                break
        
if players == 4:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")
    player4 = input("Enter player 4's name: ")

    print(f"Hello {player1}, {player2}, {player3} and {player4}!")

    while True:
        print(f"{player1}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player1_points >= TARGET_SCORE:
                print(f"{player1.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player1_points += current_points
                        print(f"Total points of {player1} are: {player1_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player1_points += current_points
                print(f"Total points of {player1} are: {player1_points}")
                break
    
        print(f"{player2}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player2_points >= TARGET_SCORE:
                print(f"{player2.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player2_points += current_points
                        print(f"Total points of {player2} are: {player2_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player2_points += current_points
                print(f"Total points of {player2} are: {player2_points}")
                break
        
        print(f"{player3}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player3_points >= TARGET_SCORE:
                print(f"{player3.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player3_points += current_points
                        print(f"Total points of {player3} are: {player3_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player3_points += current_points
                print(f"Total points of {player3} are: {player3_points}")
                break
    
        print(f"{player4}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player4_points >= TARGET_SCORE:
                print(f"{player3.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player4_points += current_points
                        print(f"Total points of {player4} are: {player4_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player4_points += current_points
                print(f"Total points of {player4} are: {player4_points}")
                break

if players == 5:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")
    player4 = input("Enter player 4's name: ")
    player5 = input("Enter player 5's name: ")

    print(f"Hello {player1}, {player2}, {player3}, {player4} and {player5}!")

    while True:
        print(f"{player1}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player1_points >= TARGET_SCORE:
                print(f"{player1.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player1_points += current_points
                        print(f"Total points of {player1} are: {player1_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player1_points += current_points
                print(f"Total points of {player1} are: {player1_points}")
                break
    
        print(f"{player2}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player2_points >= TARGET_SCORE:
                print(f"{player2.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player2_points += current_points
                        print(f"Total points of {player2} are: {player2_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player2_points += current_points
                print(f"Total points of {player2} are: {player2_points}")
                break
        
        print(f"{player3}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player3_points >= TARGET_SCORE:
                print(f"{player3.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player3_points += current_points
                        print(f"Total points of {player3} are: {player3_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player3_points += current_points
                print(f"Total points of {player3} are: {player3_points}")
                break
        
        print(f"{player4}'s turn!")
        input("Press enter to roll!")

        current_points = 0

        while True:
            if player4_points >= TARGET_SCORE:
                print(f"{player4.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player4_points += current_points
                        print(f"Total points of {player4} are: {player4_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player4_points += current_points
                print(f"Total points of {player4} are: {player4_points}")
                break
        
    print(f"{player5}'s turn!")
    input("Press enter to roll!")

    current_points = 0

    while True:
            if player5_points >= TARGET_SCORE:
                print(f"{player5.upper()} WINS!")
                quit()

            num = roll()

            print(f"You got {num}")

            if num != 1:
                current_points += num
                print(f"Current points you will get if you stop rolling: {current_points}")
            
                while True:
                    again = input("Do you want to roll again?: ").lower()

                    if again == "yes":
                        roll_again = True
                        break

                    elif again == "no":
                        player5_points += current_points
                        print(f"Total points of {player5} are: {player5_points}")
                        roll_again = False
                        break

                    else:
                        print("Please type yes or no")
                
                if roll_again:
                    continue
                else:
                    break
            
            else:
                print("Oops! you lost all the gained points")
                current_points = 0
                roll_again = False
                player5_points += current_points
                print(f"Total points of {player5} are: {player5_points}")
                break