def fibbonaci(num):
    f = 0
    s = 1
    list1 = [f, s]
    print(0)
    print(1)
    for i in range(num - 2):
        last = list1[-1]
        second_last = list1[-2]
        next = last + second_last
        list1.extend([next])
        print(next)

while True:
    first_nums = input("How many numbers do you want in your fibbonaci sequence?: ")
    if first_nums.isdigit():
        first_nums = int(first_nums)
        break
    else:
        print("Please type in a number")

print(f"The first {first_nums} numbers of the fibbonaci sequence are:")
fibbonaci(first_nums)