#### Iteration 1  - Popcorn  ####
subtotal = 0

# Variables
# ------------ #
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

size = input("""
What size of popcorn do you want?
    [s]mall  - $5.00
    [m]edium - $6.00
    [l]arge  - $7.00
    [n]one   - $0.00
> """).lower()

if size == "none" or size == "n":
    subtotal += 0
    popcornSize = ""
elif size == "small" or size == "s":
    subtotal += 5
    popcornSize = "Small"
elif size == "medium" or size == "m":
    subtotal += 6
    popcornSize = "Medium"
elif size == "large" or size == "l":
    subtotal += 7
    popcornSize = "Large"
else:
    print("Invalid Size Entered")

print(f"Subtotal: ${subtotal:.2f}")

#### Iteration 2  - Soda Pop ####
wantsSoda = input("Do you want a soda? [yes/no]\n> ")

if wantsSoda == "yes" or wantsSoda == "y":
    sodaSize = input("""
What size of soda do you want?
    [s]mall  - $3.00
    [m]edium - $4.00
    [l]arge  - $5.00
> """).lower()

    if sodaSize == "small" or sodaSize == "s":
        subtotal += 3
        sodaSize = "Small"
    elif sodaSize == "medium" or sodaSize == "m":
        subtotal += 4
        sodaSize = "Medium"
    elif sodaSize == "large" or sodaSize == "l":
        subtotal += 5
        sodaSize = "Large"

        wantsChild = input("Do you want a child size for $0.38? [yes/no]\n> ").lower()

        if wantsChild == "yes" or wantsChild == "y":
            subtotal += 0.38
        elif wantsChild == "no" or wantsChild == "n":
            print("")
        else:
            print("Invalid response")

    else:
        print("Invalid Soda Size Entered")
elif wantsSoda == "no" or wantsSoda == "n":
    sodaSize = ""
else:
    print("Invalid response")

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

print(f"Subtotal: ${subtotal:.2f}")
print(f"Candy Flavor: {candyFlavor}")

#### Iteration 4  - Butter   ####
butterPumps = int(input(
"""How much butter do you want? Each pump is $0.25.
> """))

butterPrice = butterPumps * 0.25
subtotal += butterPrice
print(f"Subtotal: ${subtotal:.2f}")

#### Iteration 5  - Checkout Screen ####
discount = 0 
if popcornSize and sodaSize and candyFlavor:
    discount = 1.50
    subtotal -= discount
    if subtotal < 0:
        subtotal = 0

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
