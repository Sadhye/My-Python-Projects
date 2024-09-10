# FUNCTIONS

def hcf(x, y):
    hcf = 1
    
    if x < y:
        smaller = x
    elif x > y:
        smaller = y
    else:
        return x

    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    
    return hcf

def simplify_fraction(numerator, denominator):
    hcf_value = hcf(numerator, denominator)

    simplified_numerator = numerator / hcf_value
    simplified_denominator = denominator / hcf_value

    return simplified_numerator, simplified_denominator

# MAIN CODE

while True:
    while True:
        numerator = input("Enter the numerator of the fraction: ")

        if numerator.isdigit():
            numerator = int(numerator)
            break
        else:
            print("Please type a positive integer")
    
    while True:
        denominator = input("Enter the denominator of the fraction: ")

        if denominator.isdigit():
            denominator = int(denominator)
            break
        else:
            print("Please type a positive integer")
    
    try:
        simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)

    except ZeroDivisionError:
        print("Cannot divide by 0")
        continue

    user_fraction = f"{numerator}/{denominator}"
    simplified_fraction = f"{int(simplified_numerator)}/{int(simplified_denominator)}"

    if user_fraction == simplified_fraction:
        print(f"The fraction {user_fraction} is already in its simplest form")
    else:
        print(f"{user_fraction} simplified is {simplified_fraction}")
    
    while True:
        again = input("Do you want to simplify another fraction?: ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("Okay, bye :)")
            quit()
        else:
            print("Please type yes or no")

    continue