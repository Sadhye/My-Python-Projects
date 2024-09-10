import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "pineapple", "watermelon", "peach", "mango"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            attempts += 1
            print("Incorrect guess. You have {} attempts left.".format(max_attempts - attempts))

        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word: '{}'".format(word_to_guess))
            break
        elif attempts == max_attempts:
            print("Sorry, you've run out of attempts. The word was '{}'.".format(word_to_guess))
            break

if __name__ == "__main__":
    hangman()