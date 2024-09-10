import random
import time

operators = ["+", "-", "*"]
operands = range(3, 12)
wrong = 0

def generate_problem():
    left = random.randint(3, 12)
    right = random.randint(3, 12)
    operator = random.choice(operators)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(10):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
    
print("----------------------")
print("Nice work! You finished in", total_time, "seconds")