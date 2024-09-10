def factor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Please type in a number")

print("The factors of", num, "are:")
factor(num)