def sqrt(num):
    for i in range(num):
        if i * i == num:
            sqrt = i
    return sqrt

while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Please type in a number")

print("The square root of", num, "is", sqrt(num))