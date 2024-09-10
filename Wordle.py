import random

words = ["guitar", "piano", "table", "phone"]
random_word = random.choice(words)
chances = 5

print("WORDLE (NOT REALLY)\n")

if random_word == "guitar":
    while True:
        if chances == 0:
            print("You ran out of chances. The word was guitar.")
            break

        word = input("Guess the 6 letter word: ").lower()

        if len(word) != 6:
            print("Please type a 6 letter word")
            continue

        elif word == "guitar":
            print("Yes! The word was guitar.")
            break

        else:
            for i in word:
                if i in "guitar":
                    print(f"{i} is in the word")
            chances -= 1
            print(f"You currently have {chances} chances left")

if random_word == "piano":
    while True:
        if chances == 0:
            print("You ran out of chances. The word was piano.")
            break

        word = input("Guess the 5 letter word: ").lower()

        if len(word) != 5:
            print("Please type a 5 letter word")
            continue

        elif word == "piano":
            print("Yes! The word was piano.")
            break

        else:
            for i in word:
                if i in "piano":
                    print(f"{i} is in the word")
            chances -= 1
            print(f"You currently have {chances} chances left")

if random_word == "table":
    while True:
        if chances == 0:
            print("You ran out of chances. The word was table.")
            break

        word = input("Guess the 5 letter word: ").lower()

        if len(word) != 5:
            print("Please type a 5 letter word")
            continue

        elif word == "table":
            print("Yes! The word was table.")
            break

        else:
            for i in word:
                if i in "table":
                    print(f"{i} is in the word")
            chances -= 1
            print(f"You currently have {chances} chances left")

if random_word == "phone":
    while True:
        if chances == 0:
            print("You ran out of chances. The word was phone.")
            break

        word = input("Guess the 5 letter word: ").lower()

        if len(word) != 5:
            print("Please type a 5 letter word")
            continue

        elif word == "phone":
            print("Yes! The word was phone.")
            break

        else:
            for i in word:
                if i in "phone":
                    print(f"{i} is in the word")
            chances -= 1
            print(f"You currently have {chances} chances left")