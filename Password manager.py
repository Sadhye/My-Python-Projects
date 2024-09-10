while True:
    mp = input("Enter the master password: ")
    if mp == "BakshiFamily3":
        break
    else:
        print("Wrong password!")

passwords = []
accounts = []

while True:
    mode = input("Do you want to view or add a password?: ").lower()
    if mode == "add":
        acc = input("Acoount Name: ")
        if acc in accounts:
            print(f"An account named {acc} already exists")
            while True:
                replace = input(f"Do you want to change the password of {acc}?: ").lower()
                if replace == "no":
                    continue_outer_loop = True
                    replace_pass = False
                    break
                elif replace == "yes":
                    continue_outer_loop = False
                    replace_pass = True
                    break
                else:
                    print("Please type yes or no")
                    continue
            if continue_outer_loop:
                continue
        else:
            replace_pass = False
            accounts.append(acc)
            
        pwd = input("Password: ")
        pm = f"{acc}|{pwd}"
        if replace_pass:
            acco = acc
            for i, acco in enumerate(passwords):
                if acco in passwords:
                    index = i
            passwords[index] = pm
        else:
            passwords.append(pm)
    elif mode == "view":
        print("Here are the currently saved passwords:")
        for i in passwords:
            print(i)
        continue
    else:
        print("Please type view or add")
        continue