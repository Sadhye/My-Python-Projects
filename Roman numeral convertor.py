roman_numbers = {1000 : "M",
                 999 : "IM"
                 900 : "CM",
                 500 : "D",
                 400 : "CD",
                 100 : "C",
                 900 : ""
                 50 : "L",
                 10 : "X",
                 5 : "V",
                 1 : "I"}

def roman(num):
    roman_num = ""
    while num > 0:
        for i in sorted(roman_numbers.keys(), reverse=True):
            while num >= i:
                roman_num += roman_numbers.get(i)
                num -= i
    return roman_num

while True:
    while True:
        num = input("Enter a number: ")

        if num.isdigit():
            num = int(num)
        else:
            print("Please type a positive integer")
            continue
        if num > 0:
            break
        else:
            print("There is no representation for the number 0 in roman numerals")
    
    print(f"{num} in roman numerals is {roman(num)}")

    while True:
        again = input("Do you want to convert another number?: ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("Okay, bye :)")
            quit()
        else:
            print("Please type yes or no")
        
    continue