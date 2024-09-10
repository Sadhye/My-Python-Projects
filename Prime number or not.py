def prime(num):
    list1 = []
    for i in range(1, num + 1):
        if num % i == 0:
            list1.extend([i])
    if len(list1) == 2:
        print(num, "is a prime number")
    else:
        print(num, "is a composite number")

while True:
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Please type in  a number")

    if num == 1:
        print("1 is neither a prime number nor a composite number")
    else:
        prime(num)
    
    while True:
        again = input("Do you want to know another number? (Type yes or no): ").lower()
        if again == "yes":
            continue_loop = True
            break
        
        elif again == "no":
            continue_loop = False
            print("Okay, bye :)")
            break

        else:
            print("Please type yes or no")
    
    if continue_loop:
        continue
    else:
        break