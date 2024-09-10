import random
import time

print("WORD SCRAMBLE\n")

words = ["apple", "mango", "watermelon", "pineapple", "orange", "banana", "cherry", "grape", "kiwi", "peach", "strawberry", "lemon", "blueberry", "raspberry", "pomegranate"]
random_word = random.choice(words)
chances = 5

def scramble(word):
    characters = list(word)
    random.shuffle(characters)
    scrambled_word = "".join(characters)
    return scrambled_word

scrambled_word = scramble(random_word)

print(scrambled_word)

start_time = time.time()

while True:
    if chances == 0:
        print("Oops! You ran out of chances")
        print(f"The word was {random_word}")
        quit()

    user = input("Unscramble the word: ").lower()

    if len(user) != len(random_word):
        print(f"Please type a {len(random_word)} letter word")
        continue

    for i in user:
        if i not in random_word:
            print("There can't be letters that are not in the word")
            again = True
            break

        else:
            again = False
            break
    
    if again:
        continue

    if user != random_word:
        chances -= 1
        print("Oops! that's not the word")
        print(f"You have {chances} chances left")
        continue
    else:
        print(f"YES! THE WORD WAS {random_word.upper()}")
        end_time = time.time()
        break

total_time = round(end_time - start_time, 2)
print(f"You guessed the word in {total_time} seconds")