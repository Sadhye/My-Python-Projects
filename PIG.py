import random

player1_points = 0
player2_points = 0
player3_points = 0
player4_points = 0
player5_points = 0
player6_points = 0

def roll():
    random_num = random.randint(1, 6)
    return random_num

while True:
    players = input("Enter number of players (2 - 6): ")
    if players.isdigit:
        players = int(players)
        break
    else:
        print("Input is not numeric... Try again")
        continue
    
    if int(players) in range(2, 7):
        break
    else:
        print("There can only be 2 - 6 players... Try again")
        continue
    
if players == 2:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    print("Hello", player1, "and", player2 + "!")
    
    while True:
        print(player1 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player1_points += num
                print("Current points are", player1_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player1_points = 0
                print("Current points are", player1_points)
                break
        
            if player1_points >= 100:
                print(player1.upper(), "WINS!!!!!!")
                quit()

        print(player2 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player2_points += num
                print("Current points are", player2_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player2_points = 0
                print("Current points are", player2_points)
                break
        
            if player2_points >= 100:
                print(player2.upper(), "WINS!!!!!!")
                quit()

if players == 3:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")
    print("Hello", player1 + ",", player2, "and", player3 + "!")
    
    while True:
        print(player1 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player1_points += num
                print("Current points are", player1_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player1_points = 0
                print("Current points are", player1_points)
                break
        
            if player1_points >= 100:
                print(player1.upper(), "WINS!!!!!!")
                quit()

        print(player2 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player2_points += num
                print("Current points are", player2_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player2_points = 0
                print("Current points are", player2_points)
                break
        
            if player2_points >= 100:
                print(player2.upper(), "WINS!!!!!!")
                quit()
        
        print(player3 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player3_points += num
                print("Current points are", player3_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player3_points = 0
                print("Current points are", player3_points)
                break
        
            if player3_points >= 100:
                print(player3.upper(), "WINS!!!!!!")
                quit()

if players == 4:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")
    player4 = input("Enter player 4's name: ")
    print("Hello", player1 + ",", player2 + ",", player3, "and", player4)
    
    while True:
        print(player1 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player1_points += num
                print("Current points are", player1_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player1_points = 0
                print("Current points are", player1_points)
                break
        
            if player1_points >= 100:
                print(player1.upper(), "WINS!!!!!!")
                quit()

        print(player2 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player2_points += num
                print("Current points are", player2_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player2_points = 0
                print("Current points are", player2_points)
                break
        
            if player2_points >= 100:
                print(player2.upper(), "WINS!!!!!!")
                quit()
        
        print(player3 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player3_points += num
                print("Current points are", player3_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player3_points = 0
                print("Current points are", player3_points)
                break
        
            if player3_points >= 100:
                print(player3.upper(), "WINS!!!!!!")
                quit()
        
        print(player4 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player4_points += num
                print("Current points are", player4_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player4_points = 0
                print("Current points are", player4_points)
                break
        
            if player4_points >= 100:
                print(player4.upper(), "WINS!!!!!!")
                quit()

if players == 5:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")
    player4 = input("Enter player 4's name: ")
    player5 = input("Enter player 5's name: ")
    print("Hello", player1 + ",", player2 + ",", player3 + ",", player4, "and", player5 + "!")
    
    while True:
        print(player1 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player1_points += num
                print("Current points are", player1_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player1_points = 0
                print("Current points are", player1_points)
                break
        
            if player1_points >= 100:
                print(player1.upper(), "WINS!!!!!!")
                quit()

        print(player2 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player2_points += num
                print("Current points are", player2_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player2_points = 0
                print("Current points are", player2_points)
                break
        
            if player2_points >= 100:
                print(player2.upper(), "WINS!!!!!!")
                quit()
        
        print(player3 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player3_points += num
                print("Current points are", player3_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player3_points = 0
                print("Current points are", player3_points)
                break
        
            if player3_points >= 100:
                print(player3.upper(), "WINS!!!!!!")
                quit()
        
        print(player4 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player4_points += num
                print("Current points are", player4_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player4_points = 0
                print("Current points are", player4_points)
                break
        
            if player4_points >= 100:
                print(player4.upper(), "WINS!!!!!!")
                quit()
        
        print(player5 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player5_points += num
                print("Current points are", player5_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player5_points = 0
                print("Current points are", player5_points)
                break
        
            if player5_points >= 100:
                print(player5.upper(), "WINS!!!!!!")
                quit()

if players == 6:
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    player3 = input("Enter player 3's name: ")
    player4 = input("Enter player 4's name: ")
    player5 = input("Enter player 5's name: ")
    player6 = input("Enter player 6's name: ")
    print("Hello", player1 + ",", player2 + ",", player3 + ",", player4 + ",", player5, "and", player6 + "!")
    
    while True:
        print(player1 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player1_points += num
                print("Current points are", player1_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player1_points = 0
                print("Current points are", player1_points)
                break
        
            if player1_points >= 100:
                print(player1.upper(), "WINS!!!!!!")
                quit()

        print(player2 + "'s turn!")
    
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player2_points += num
                print("Current points are", player2_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player2_points = 0
                print("Current points are", player2_points)
                break
        
            if player2_points >= 100:
                print(player2.upper(), "WINS!!!!!!")
                quit()
        
        print(player3 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player3_points += num
                print("Current points are", player3_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player3_points = 0
                print("Current points are", player3_points)
                break
        
            if player3_points >= 100:
                print(player3.upper(), "WINS!!!!!!")
                quit()
        
        print(player4 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player4_points += num
                print("Current points are", player4_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player4_points = 0
                print("Current points are", player4_points)
                break
        
            if player4_points >= 100:
                print(player4.upper(), "WINS!!!!!!")
                quit()
        
        print(player5 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player5_points += num
                print("Current points are", player5_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player5_points = 0
                print("Current points are", player5_points)
                break
        
            if player5_points >= 100:
                print(player5.upper(), "WINS!!!!!!")
                quit()
        
        print(player6 + "'s turn!")
        
        while True:
            num = roll()
            print("You got", num)
            if not num == 1:
                player6_points += num
                print("Current points are", player6_points)
                again = input("Do you want to roll again?: ").lower()
                if again == "yes":
                    continue
                if again == "no":
                    break
        
            if num == 1:
                player6_points = 0
                print("Current points are", player6_points)
                break
        
            if player6_points >= 100:
                print(player6.upper(), "WINS!!!!!!")
                quit()