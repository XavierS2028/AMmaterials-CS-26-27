# Bander - ConcessionStand.py

#### GLOBAL VARIABLES ####
subtotal = 0
discount = ""
order = []

# === === === === === === === === === === 
#### HELPER FUNCTIONS ####

def userInput(question, answers):
    userAnswer = input(question)

    while not(userAnswer in answers):
        userAnswer = input(question)

    return userAnswer

# categeory - string
# option1   - tuple of format (name:string, letter:char, price:float)
# option2   - tuple of format (name:string, letter:char, price:float)
# option3   - tuple of format (name:string, letter:char, price:float)
def orderItem3Options(category, option1, option2, option3):
    selectedOption = ""

    # Ask if user wants the item
    wantsItem = userInput(f"Do you want a {category}? ",
                          ["yes", "y", "no", "n"])
    if (wantsItem == "yes") or (wantsItem == "y"):
        selectedOption = userInput(
f"""What type of {category} do you want?
    ({option1[1]}) {option1[0]} = ${option1[2]:.2f}
    ({option2[1]}) {option2[0]} = ${option2[2]:.2f}
    ({option3[1]}) {option3[0]} = ${option3[2]:.2f}
> """, [option1[1], option2[1], option3[1]])

orderItem3Options("popcorn", ("small", "s", 1), ("medium", "m", 2), ("large", "l", 3))

def checkForDiscountAndApply(order):
    if not("n" in order) :
        subtotal -= 1
        discount = "$1.00"

def checkout(order):
    # Show Order
    print(
f"""Your Order:
    popcorn  = {order[0]}
    drink    = {order[1]}
    candy    = {order[2]}
    butter # = {order[3]}
""")
    
    checkForDiscountAndApply(order)

    print(
f"""\tdiscount = {discount}
""")

    # Show Tax
    print(
f"""subtotal = ${subtotal:.2f}
tax = ${subtotal * .07:.2f}
""")

    # Show Total
    print(f"total = {subtotal * 1.07:.2f}")
   
#=== === === === === === === === === === === === === === === 

#loop the entire process until the user is done ordering? aka multiple orders?
orderagain="y"
while(orderagain=="y"):
    #iteration 1 - popcorn
    
    orderItem3Options("popcorn", ("small", "s", 1), ("medium", "m", 2), ("large", "l", 3))

    if ui == "s":
        subtotal+=5
    elif ui == "m":
        subtotal+=6
    elif ui == "l":
        subtotal+=7
    else:
        print("No Popcorn, but why?")
    order.append(ui)               #appending or adding to the order their popcorn order
    print(f"subtotal: ${subtotal}")

    #iteration 2 - soda pop
    userInput = input("Would you like a drink? (y/n)").lower()
    if userInput=="y":
        userInput = input('''
    What size soda do you want?
        (s) small = $3.00
        (m) medium = $4.00
        (l) large = $5.00
    ''')
        if userInput=="s":
            subtotal+=3
        elif userInput=="m":
            subtotal+=4
        elif userInput =="l":
            subtotal+=5
            if input("Would you like a child size for .38 more? (y/n)?")=="y":
                subtotal+=.38
                userInput = "c"
    order.append(userInput)               #appending or adding to the order their popcorn order
    print(f"subtotal: ${subtotal:.2f}")    #:.2f means 2 floating points

    #iteration 3 - candy
    flavors=""
    candy = input("Do you want any candy? (y/n)")
    if candy == "y":
        candy = input('''
    What type of candy would you like?
        (m) M&M's - 2.50
        (s) Skittles - 2.50
        (w) World's Finest Chocolate Bars - 2
        (r) Reece's - 2
        (n) Nerds gummi clusters - 3
    ''')

        if candy == "m" or candy == "s":
            subtotal +=2.5
            if candy == "m":
                flavors = '''
        (pl) plain 
        (pe) peanut 
        (pb) peanut butter
        (mi) mini
                '''
            else:
                flavors='''
        (r) regular
        (t) tropical
                '''
                
        elif candy in "wr":
            subtotal +=2
            if candy == "w":
                flavors = '''
        (wa) wafer
        (mc) milk chocolate
        (dc) dark chocolate
        (al) almonds
        (ca) caramel
            '''
        elif candy == "n":
            subtotal+=3

        if flavors != "":
            candy=input(f"Which flavor? {flavors}")
    order.append(candy)
    print(f"subtotal: ${subtotal:.2f}")    #:.2f means 2 floating points  


    #iteration 4 - butter
    butter = input("How many butters " )   #input is ALWAYS a string
    subtotal += int(butter)*.25           #convert the string to an int
    order.append(butter)
    print(f"subtotal: ${subtotal:.2f}")    #:.2f means 2 floating points  

    print(order)    #this is for testing, need to delete out later....  
    #iteration 5 - checkout screen
    checkout(order)

    orderagain=input("Need another order? (y/n)")
