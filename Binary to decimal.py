def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

while True:
    binary_num = input("Enter a binary number or quit: ")

    if not binary_num.isdigit():
        h
    print("Decimal equivalent:", binary_to_decimal(binary_num))