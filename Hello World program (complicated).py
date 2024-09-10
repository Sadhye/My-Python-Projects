def reverse_string(s):
    return s[::-1]

def add_exclimation(s):
    return s + "!"

def main():
    string = "dlroW ,olleH"
    reversed_s = reverse_string(string)
    add_e = add_exclimation(reversed_s)
    print(add_e)

if __name__ == "__main__":
    main()