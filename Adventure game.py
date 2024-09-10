print("Hello there! Welcome to our adventure made by Sadhye and Akshit.")
print("Let's start!")
print("You are travelling in a car and you see a ship.")
ship = input("Would you like to travel by car or ship?: ").lower()

if ship == "car":
    print("You see a flyover.")
    flyover = input("Would you like to go under or over?: ").lower()
    if flyover == "over":
        print("You reach home")
        quit()
    
    if flyover == "under":
        print("The path is under construction")
        print("WARNING! Petrol is over")
        petrol = input("Do you call car service or petrol pump?: ").lower()
        if petrol == "petrol pump":
            print("Your gas is filled and you reach home")
            quit()
        
        if petrol == "car service":
            print("They are not picking up the call")
            print("You lose!")
            quit()

if ship == "ship":
    bridge = input("Do you go straight or under the bridge?: ").lower()
    if bridge == "under the bridge":
        print("You reached India!")
        print("You met a boy and he's from your country.")
        quit()
    
    if bridge == "straight":
        print("You reached Russia!")
        print("You saw an Indian guy.")
        talk = input("Will you talk to him?: ").lower()
        if talk == "yes":
            print("You got bored of him and he wasted your time and you could not go home.")
            quit()
        
        if talk == "no":
            print("You went to a restaurant and ate some food")
            print("You were going back to the ship")
            print("But a man offered you a free movie ticket.")
            ticket = input("Do you take the ticket?: ").lower()
            if ticket == "yes":
                print("You went to watch a movie.")
                quit()
            
            if ticket == "no":
                print("You went back home.")
                quit()