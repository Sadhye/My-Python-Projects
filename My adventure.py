print("Hello! Welcome to my adventure game!")

while True:
    playing = input("Do you want to play?: ").lower()
    if playing == "yes":
        print("Okay, Let's play :)")
        print("Btw, pls press enter to go to next line :)")
        break
    elif playing == "no":
        print("Okay, Goodbye :)")
        quit()
    else:
        print("Please type yes or no")

input("You were coming back from the store at night")
input("You saw a hallway and you decided to go inside")
input("You see an adorable cat with golden eyes in a cardboard box")
input("The cat was not doing anything. Not even coming out of the box")
input("It was acting suspicious. Like it was waiting for you to make a move")
while True:
    answers_cat = ["yes", "no"]
    cat = input("Do you take the cat home?: ").lower()
    if cat not in answers_cat:
        print("Please type yes or no")
        continue
    if cat == "yes":
        input("You went to back to the shop to get some cat food and went back home with the cat")
        input("When you gave the cat the food, he was'nt eating it")
        input("You thought that you wasted money buying the cat food")
        input("You were making a sandwich for yourself and you cut your hand when cutting vegetables")
        input("You went to the bathroom to clean the cut")
        input("When you came back to the kichen, you saw that the cat was licking the blood on the knife")
        