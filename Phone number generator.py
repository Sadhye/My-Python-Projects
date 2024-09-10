import random
def phone_number():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10):
        print(random.choice(nums), end="")

phone_number()