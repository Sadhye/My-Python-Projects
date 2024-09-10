import random

print("24 GAME\n")

print("Rules:")
print("1. You will be given 4 random numbers between the range from 1 to 9")
print("2. Use the 4 numbers in a calculation with the basic arithmetic operators (+ - * /) to get as close to the number 24")
print("3. Enjoy!\n")

def generate_random_nums():
    list_of_nums = []

    for _ in range(4):
        num = random.randint(1, 9)
        list_of_nums.append(num)

    return list_of_nums

original_nums = generate_random_nums()

print("Here are the 4 random numbers:")

for i in original_nums:
    print(i)

print()

while True:
    calculation = input("Use these in a calculation to get as close to 24: ")

    try:
        result = eval(calculation)
        player_nums = []

        for num in calculation.split():
            if num.isdigit():
                player_nums.append(int(num))
            
        if set(player_nums) == set(original_nums):
            if result % 1 == 0:
                result = int(result)

            if result == 24:
                print("CONGRATS! YOU GOT 24!")
            else:
                print(f"You got {result}")
                difference = abs(24 - result)
                print(f"You were {difference} close to 24")
                break
            
        else:
            print("You did not use the numbers given")
            continue

    except:
        print("Invalid calculation")