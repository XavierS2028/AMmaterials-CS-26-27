#### Iteration 1  - Popcorn  ####
subtotal = 0

size = input("""
What size of popcorn do you want?
    [s]mall  - $5.00
    [m]edium - $6.00
    [l]arge  - $7.00
    [n]one   - $0.00
> """).lower()

if size == "none" or size == "n":
    subtotal += 0
elif size == "small" or size == "s":
    subtotal += 5
elif size == "medium" or size == "m":
    subtotal += 6
elif size == "large" or size == "l":
    subtotal += 7
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
    elif sodaSize == "medium" or sodaSize == "m":
        subtotal += 4
    elif sodaSize == "large" or sodaSize == "l":
        subtotal += 5

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
    print("")
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
        subtotal += 2.5
    elif candyType == "w" or candyType == "r":
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

#### Iteration 4  - Butter   ####
