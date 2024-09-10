print("Hello there! Welcome to our football quiz by Sadhye and Akshit")
marks = 0
print("-----------------------------------")
print("Which player has most goals in football history?")
print("a: Cristiano Ronaldo")
print("b: Pelé")
print("c: Neymar Jr.")
print("d: Erling Halland")
q1 = input("Ans (Type a, b, c or d): ").lower()
if q1 == "b":
    print("Correct!")
    marks += 1
    print("-----------------------------------")
else:
    print("No, it was b: Pelé")
    print("-----------------------------------")

print("What is the full name of Pelé?")
print("a: Pelé")
print("b: Pelé de Silva")
print("c: Santos Pelé Jr.")
print("d: Edson Arantes do Nascimento")
q2 = input("Ans (Type a, b, c or d): ").lower()
if q2 == "d":
    print("Correct!")
    marks += 1
    print("-----------------------------------")
else:
    print("No, it was d: Edson Arantes do Nascimento")
    print("-----------------------------------")

print("Who is having the record of most goals in a calendar year?")
print("a: Messi")
print("b: Pelé")
print("c: Ronaldo Nazario")
print("d: Lewandowski")
q3 = input("Ans (Type a, b, c or d): ").lower()
if q3 == "a":
    print("Correct!")
    marks += 1
    print("-----------------------------------")
else:
    print("No, the answer was a: Messi")
    print("-----------------------------------")

print("Which team has most champion league trophies?")
print("a: Barcelona")
print("b: Real Madrid")
print("c: Liverpool")
print("d: Atletico Madrid")
q4 = input("Ans (Type a, b, c or d): ").lower()
if q4 == "b":
    print("Correct!")
    marks += 1
    print("-----------------------------------")
else:
    print("No, the answer was b: Real Madrid")
    print("-----------------------------------")

print("Who won the FIFA World Cup as a captain?")
print("a: Kilyan Mbappé")
print("b: Oliver Giroud")
print("c: Pavard")
print("d: N'golo Kante")
q5 = input("Ans (Type a, b, c or d): ").lower()
if q5 == "b":
    print("Correct!")
    marks += 1
    print("-----------------------------------")
else:
    print("No, the answer was b: Oliver Giroud")
    print("-----------------------------------")

print("You got", marks, "out of 5 questions correct")
print("Thank you for playing the quiz")
print("Goodbye!")