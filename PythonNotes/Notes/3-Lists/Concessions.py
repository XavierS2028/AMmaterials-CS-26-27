#### Iteration 1  - Popcorn  ####

# Variables
# ------------ #
order = []
subtotal = 0

popcornSize = ""
popcornCost = 0 

sodaSize = ""
sodaCost = 0
hasChild = False
childPrice = 0

candyFlavor = ""
candyPrice = 0

butterPumps = 0
butterPrice = 0

# ------------- #

userInput = input("""
What size of popcorn do you want?
    [s]mall  - $5.00
    [m]edium - $6.00
    [l]arge  - $7.00
    [n]one   - $0.00
> """).lower()

if userInput == "none" or userInput == "n":
    subtotal += 0
    order.append("none")
elif userInput == "small" or userInput == "s":
    subtotal += 5
    order.append("small")
elif userInput == "medium" or userInput == "m":
    subtotal += 6
    order.append("medium")
elif userInput == "large" or userInput == "l":
    subtotal += 7
    order.append("large")
else:
    print("Invalid Size Entered")
    order.append("error")

print(f"Subtotal: ${subtotal:.2f}")

#### Iteration 2  - Soda Pop ####
userInput = input("Do you want a soda? [yes/no]\n> ")

if userInput == "yes" or userInput == "y":
    userInput = input("""
What size of soda do you want?
    [s]mall  - $3.00
    [m]edium - $4.00
    [l]arge  - $5.00
> """).lower()

    if userInput == "small" or userInput == "s":
        subtotal += 3
        order.append("small")
    elif userInput == "medium" or userInput == "m":
        subtotal += 4
        order.append("medium")
    elif userInput == "large" or userInput == "l":
        subtotal += 5
        order.append("large")

        wantsChild = input("Do you want a child size for $0.38? [yes/no]\n> ").lower()

        if wantsChild == "yes" or wantsChild == "y":
            subtotal += 0.38
        elif wantsChild == "no" or wantsChild == "n":
            print("")
        else:
            print("Invalid response")

    else:
        print("Invalid Soda Size Entered")
elif userInput == "no" or userInput == "n":
    order.append("none")
else:
    print("Invalid response")
    order.append("error")

order.append(sodaSize)

print(f"Subtotal: ${subtotal:.2f}")

#### Iteration 3  - Candy    ####
wantsCandy = input("Do you want any candy? [yes/no]\n> ")

if wantsCandy == "yes" or wantsCandy == "y":
    candyType = input(
"""What type of candy do you want?
    [M]&M's                    - $2.50
    [S]kittles                 - $2.50
    [W]orld's Finest Chocolate - $2.00
    [R]eeces                   - $2.00
    [N]erds                    - $3.00
> """).lower()
    
    if candyType == "m" or candyType == "s":
        if candyType == "m":
            flavor = input("""
                What flavor do you want?
                    [P]lain
                    P[e]anut
                    Peanut [B]utter
                    [M]ini
                > """).lower()

            if flavor == "p":
                candyFlavor = "Plain M&Ms"
            elif flavor == "e":
                candyFlavor = "Peanut M&Ms"
            elif flavor == "b":
                candyFlavor = "Peanut Butter M&Ms"
            elif flavor == "m":
                candyFlavor = "Mini M&Ms"
            else:
                print("Invalid M&M Type")

        elif candyType == "s":
            flavor = input("""
                What flavor do you want?
                    [R]egular
                    [T]ropical
                > """).lower()

            if flavor == "r":
                candyFlavor = "Regular Skittles"
            elif flavor == "t":
                candyFlavor = "Tropical Skittles"
            else:
                print("Invalid Skittle Type")

        subtotal += 2.5

    elif candyType == "w" or candyType == "r":
        if candyType == "w":
            flavor = input(
"""What flavor do you want?
    [W]afer
    [M]ilk Chocolate
    [D]ark Chocolate
    [A]lmonds
    [C]aramel
> """).lower()
            
            if flavor == "w":
                candyFlavor = "Wafer Chocolate Bar"
            elif flavor == "m":
                candyFlavor = "Milk Chocolate Bar"
            elif flavor == "d":
                candyFlavor = "Dark Chocolate Bar"
            elif flavor == "a":
                candyFlavor = "Almond Chocolate Bar"
            elif flavor == "c":
                candyFlavor = "Caramel Chocolate Bar"
            else:
                print("Invalid Chocolate Type")

        subtotal += 2
    elif candyType == "n":
        subtotal += 3
    else:
        print("Invalid Candy Input")
elif wantsCandy == "no" or wantsCandy == "n":
    print("")
else:
    print("Invalid Input")

order.append(candyType)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Candy Flavor: {candyFlavor}")

#### Iteration 4  - Butter   ####
butterPumps = int(input(
"""How much butter do you want? Each pump is $0.25.
> """))

butterPrice = butterPumps * 0.25
subtotal += butterPrice

order.append(butterPumps)

print(f"Subtotal: ${subtotal:.2f}")

#### Iteration 5  - Checkout Screen ####
discount = 0 
if popcornSize and sodaSize and candyFlavor:
    discount = 1.50
    subtotal -= discount
    if subtotal < 0:
        subtotal = 0

print(order)

print(
f"""Your Order:
    Popcorn: {popcornSize} - ${popcornCost:.2f}
    Drink: {sodaSize} - ${sodaCost:.2f}
    Candy: {candyFlavor} - ${candyPrice:.2f}
    Butter: {butterPumps} pumps - ${butterPrice:.2f}

    discount - ${discount:.2f}
    
    subtotal - ${subtotal:.2f}
    tax      - ${subtotal * .07:.2f}
    total    - ${subtotal * 1.07:.2f}
""")
