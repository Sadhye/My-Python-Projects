categories = ["integers", "decimals", "both"]
marks = 0

while True:
    math = input("Which topic do you want questions about? (integers, decimals or both): ").lower()
    
    if math in categories:
        break
    else:
        print("Please type integers, decimals or both")

print("-----------------------------------------------------------------")

if math == "integers":
    print("Okay, let's do integers!")
    q1 = input("What is the additive identity in integers?: ")
    if q1 == "0":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was 0")
    
    q2 = input("(-1) + (-2) = ")
    if q2 == "-3":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was -3")
        print("(-1) + (-2)")
        print("= -1 - 2")
        print("= -3")
    
    q3 = input("[(-2) x 3] + [(-2) x 5] = ")
    if q3 == "-16":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was -16")
        print("[(-2) x 3] + [(-2) x 5]")
        print("= (-6) + (-10)")
        print("= -16")
    
    q4 = input("(-3) x (-6) x (-2) x (-1) = ")
    if q4 == "36" or q4 == "+36":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was 36")
        print("(-3) x (-6) x (-2) x (-1)")
        print("= 18 x (-2) x (-1)")
        print("= (-36) x (-1)")
        print("= 36")
    
    q5 = input("[(-6) + 5] x [(-2) + 1] = ")
    if q5 == "1" or q5 == "+1":
        print("Correct!")
        marks += 1
        print("---------------------------------------------------------")
    else:
        print("No, the answer was 1")
        print("[(-6) + 5] + [(-2) + 1]")
        print("= (-1) x (-1)")
        print("= 1")
        print("---------------------------------------------------------")
    
    print("You got", marks, "out of 5 questions correct")
    print("Thank you for attempting the quiz")

if math == "decimals":
    print("Okay, let's do decimals!")
    q1 = input("2.06 + 4.009 + 3.4 = ")
    if q1 == "9.469":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was 9.469")
        print("2.06 + 4.009 + 3.4")
        print()
        print("  2.060")
        print("  4.009")
        print("+ 3.400")
        print("  _____")
        print("  9.469")
    
    q2 = input("211.02 + 4 = ")
    if q2 == "215.02":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was 215.02")
        print()
        print("  211.02")
        print("+   4.00")
        print("________")
        print("  215.02")
    
    q3 = input("9.087 + 34.998 + 223.234 = ")
    if q3 == "267.319":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was 267.319")
        print()
        print("    9.087")
        print("   34.998")
        print("+ 223.234")
        print("_________")
        print("  267.319")
    
    q4 = input("(0.9) + (8.9) + (3.4) = ")
    if q4 == "13.2":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer is 13.2")
        print()
        print("  0.9")
        print("  8.9")
        print("+ 3.4")
        print("_____")
        print(" 13.2")
    
    q5 = input("Amit bought 2.45 kg oranges, 1.34 kg mangoes and 1.98 kg apple. What is the total weight of fruits Amit bought?: ").lower()
    if q5 == "5.77 kg":
        print("Correct!")
        marks += 1
        print("---------------------------------------------------------")
    else:
        print("No, Amit got 5.77 kg of fruit")
        print()
        print("Weight of oranges = 2.45 kg")
        print("Weight of mangoes = 1.34 kg")
        print("Weight of apples = 1.98 kg")
        print("Total weight = 2.45 + 1.34 + 1.98")
        print()
        print("  2.45")
        print("  1.34")
        print("+ 1.98")
        print("______")
        print("  5.77")
        print()
        print("Amit has 5.77 kg of fruit")
        print("---------------------------------------------------------")
    
    print("You got", marks, "out of 5 questions correct")
    print("Thamk you for attempting this quiz")

if math == "both":
    print("Oh! Looks like you want a challenge!")
    q1 = input("-2.09 - 15.271 = ")
    if q1 == "-17.361" or q1 == "- 17.361":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was -17.361")
        print("-2.09 - 15.271")
        print("= -(2.09 + 15.271)")
        print("= -17.361")
    
    q2 = input("4.16 - 9.043 = ")
    if q2 == "-4.883" or q2 == "- 4.883":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was -4.833")
        print("4.16 - 9.043")
        print("= -(4.16 - 9.043)")
        print("= -4.833")
    
    q3 = input("-51 + 81.623 = ")
    if q3 == "30.623" or q3 == "+30.623" or q3 == "+ 30.623":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was 30.623")
        print("-51 + 81.623")
        print("= 81.623 - 51")
        print("= 30.623")
    
    q4 = input("-5.62 + (-12.9) = ")
    if q4 == "-18.52" or q4 == "- 18.52":
        print("Correct!")
        marks += 1
    else:
        print("No, the answer was -18.52")
        print("-5.62 + (-12.9)")
        print("= -5.62 - 12.9")
        print("= -(5.62 + 12.9)")
        print("= -18.52")
    
    q5 = input("5.23 - (-9.1) = ")
    if q5 == "14.33" or q5 == "+14.33" or q5 == "+ 14.33":
        print("Correct!")
        print("---------------------------------------------------------")
        marks += 1
    else:
        print("No, the answer was 14.33")
        print("5.23 - (-9.1)")
        print("= 5.23 + 9.1")
        print("= 14.33")
        print("---------------------------------------------------------")
    
    print(f"You got {marks} out of 5 questions correct")
    print("Thank you for attempting the quiz")

print("Goodbye!")