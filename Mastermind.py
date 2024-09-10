import random

colours = ["R", "G", "B", "Y", "W", "O"]

random_code_list = []
for i in colours:
    random_colour = random.choice(colours)
    random_code_list.append(random_colour)
random_code_str = " ".join(random_code_list)

tries = 10

print("Welcome to mastermind! Attempt to guess the 4 digit code... You have 10 tries")
print(f"The colours that could make up the code are: R G B Y W O")

while True:
    guess = input("Guess (SEPERATE CHARACTERS WITH SPACE): ").upper()

    for i in guess: