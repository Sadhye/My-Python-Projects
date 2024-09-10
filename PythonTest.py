print("Python test made in Python *skull emoji*\n")

levels = ["beginner", "intermediate", "advanced", "expert"]

while True:
    level = input("What level are you? (Beginner/Intermediate/Advanced/Expert): ").lower()

    if level not in levels:
        print("Please type beginner, intermediate, advanced or expert")
        continue
    else:
        break

if level == "beginner":
    pass