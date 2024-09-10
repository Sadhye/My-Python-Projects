def pell_numbers(num):
    pell_nums = [0, 1]
    print(0)
    print(1)
    for i in range(num - 2):
        last = pell_nums[-1] * 2
        second_last = pell_nums[-2]
        next = last + second_last
        pell_nums.append(next)
        print(next)

while True:
    nums = input("How many numbers do you want in your pell numbers?: ")
    if nums.isdigit():
        nums = int(nums)
        break
    else:
        print("Please type in a number")

print(f"The first {nums} numbers of pell numbers are:")
pell_numbers(nums)