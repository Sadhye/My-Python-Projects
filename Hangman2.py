import random

words = ["phone", "apple", "ear", "chips", "football"]
random_word = "phone" #random.choice(words)

tries = 7

letters_of_phone = ["p", "h", "o", "n", "e"]
letters_of_apple = ["a", "p", "l", "e"]
letters_of_ear = ["e", "a", "r"]
letters_of_chips = ["c", "h", "i", "p", "s"]
letters_of_football = ["f", "o", "t", "b", "a", "l"]

if random_word == "phone":
    while True:
        print("Electronic Device")
        print("_ _ _ _ _")
        letter = input("Guess a letter: ")
        if len(letter) != 1:
            print("Please type in a single letter")
            continue
        if letter not in letters_of_phone:
            tries -= 1
            if tries == 0:
                print("You lost! The word was phone")
                quit()
            else:
                print(f"Nope, you have {tries} tries left")
                continue
        if letter == "p":
            print("Yes! The word does have P")
            break
            while True:
                print("P _ _ _ _")
                letter = input("Guess a letter: ")
            