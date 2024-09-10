print("PRIME AND COMPOSITE NUMBERS BETWEEN A RANGE\n")

while True:
    num1 = input("Enter the first number in range: ")

    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print("Please type a valid number")
        continue

while True:
    num2 = input("Enter the second number in range: ")

    if num2.isdigit():
        num2 = int(num2)
    else:
        print("Please type a valid number")
        continue

    if num2 > num1:
        break
    else:
        print(f"The second number should be bigger than the first number ({num1})")

prime_nums = []
composite_nums = []

def prime(num):
    list1 = []
    for i in range(1, num + 1):
        if num % i == 0:
            list1.extend([i])
    if len(list1) == 2:
        return True
    return False

def ratio(x, y):
    if x < y:
        smaller = x
        bigger = y
    else:
        smaller = y
        bigger = x
    
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = 1
    
    ratio = f"{int(x/hcf)}:{int(y/hcf)}"
    return ratio

for i in range(num1, num2 + 1):
    if prime(i):
        prime_nums.append(i)
    else:
        composite_nums.append(i)

print(f"All the prime numbers between {num1} and {num2} are:")

for i in prime_nums:
    print(i)

print()

print(f"All composite numbers between {num1} and {num2} are:")

for i in composite_nums:
    print(i)

print()

print(f"Number of prime numbers in range: {len(prime_nums)}")
print(f"Number of composite nums in range: {len(composite_nums)}")

print()

print("Ratio of prime numbers to composite numbers:", ratio(len(prime_nums), len(composite_nums)))