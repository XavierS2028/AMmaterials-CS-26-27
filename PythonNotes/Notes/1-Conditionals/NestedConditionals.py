#### Challenge 1 ####
response1 = input("Did primary backup file generate? ")

if response1 == "yes":
    targetDest = input('Target destination: "cloud" or "nas"? ')

    if targetDest == "cloud":
        print("Check AWS S3 bucket write permissions")
    elif targetDest == "nas":
        print("Check local SMB storage quota")
    else:
        print("Invalid Input")
elif response1 == "no":
    diskState = input("Disk full or process timed out? ")

    if diskState == "full":
        print("Trigger disk cleanup alert")
    elif diskState == "timeout":
        print("Restart backup service daemon")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")   
 
#### Challenge 2 ####
role = input("Enter Role: 'student' or 'visitor' ")

if role == "student":
    hasBadge = input("Has student a badge with them? ")

    if hasBadge == "yes":
        hasWaiver = input("Lab waiver signed? ")

        if hasWaiver == "yes":
            print("Grant door badge unlock access")
        elif hasWaiver == "no":
            print("Must complete digital safety quiz before entry")
        else:
            print("Invalid Input")

    elif hasBadge == "no":
        print("Report to the office for temporary badge")

    else:
        print("Invalid Input")

elif role == "visitor":
    hasAppointment = input("Has pre-scheduled appointment? ")

    if hasAppointment == "yes":
        staffPresent = input("Staff escort present at door? ")

        if staffPresent == "yes":
            print("Issue visitor pass badge")
        elif staffPresent == "no":
            print("Must wait for escord arrival")
        else:
            print("Invalid Input")

    elif hasAppointment == "no":
        print("Direct to reception lobby waiting area")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")

#### Challenge 3 ####
didRestart = input("Did you restart the computer? ")

if didRestart == "yes":
    didRestartPC = input("Did you restart the PC or just power cycle the monitor? ")
    
    if didRestartPC == "pc":
        isEthernet = input("Is the Ethernet cable plugged into the wall? ")
        if isEthernet == "yes":
            print("It's a DNS issue. It's ALWAYS DNS. Escalate to Tier 3")
        elif isEthernet == "no":
            print("Plug it in! WiFi does not come from thin air")
        else:
            print("Invalid Input")

    elif didRestartPC == "monitor":
        print("Facepalm: Please turn off the box on the floor!")
    else:
        print("Invalid Input")

elif didRestart == "no":
    isPowerStrip = input("Is the power strip plugged into itself? ")

    if isPowerStrip == "yes":
        print("Infinite power loop: Unplug it from itself and plug it into the wall")
    elif isPowerStrip == "no":
        print("Restart it right now. Ticket closed!")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")

#### Challenge 4 ####
isHissing = input("Do you hear a Creeper hissing? [yes/no] ")

if isHissing == "yes":
    hasBucket = input("Water bucket in your hotbar? [yes/no] ")

    if hasBucket == "yes":
        print("MLG water drop: absorb 100% of blast damage!")
    elif hasBucket == "no":
        dugDown = input("Did you dig straight down? [yes/no] ")

        if dugDown == "yes":
            print("Fell into lava. Diamonds gone! Player tried to swim in lava.")
        elif dugDown == "no":
            print("Shield up! Blown 20 blocks into a ravine.")
        else:
            print("Invalid Input")

    else:
        print("Invalid Input")

elif isHissing == "no":
    isHungry = input("Is your hunger bar totally empty? [yes/no] ")

    if isHungry == "yes":
        eatFlesh = input("Eat mystery rotten flesh? [yes/no]")
        
        if eatFlesh == "yes":
            print("Hunger effect active, but you barely survived!")
        elif eatFlesh == "no":
            print("Starved to death while looking at a cow. Respawn screen!")
        else:
            print("Invalid Input")
    elif isHungry == "no":
        print("Build a 3x1 dirt pillar, crouch, and cry until dawn.")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")

#### Challenge 5 ####
isClosed = input("Is the hallway bathroom closed for 'cleaning'? [yes/no] ")

if isClosed == "yes":
    canHold = input("Can you clench & hold for 15 min? [yes/no] ")

    if canHold == "yes":
        print("PENGUIN WADDLE: Lock core, slow robot stride to homeroom class!")
    elif canHold == "no":
        willRisk = input("Risk the creepy locker room? [yes/no] ")
        
        if willRisk == "yes":
            print("DUNGEON RESTROOM: 0-ply paper & darkness. You survive!")
        elif willRisk == "no":
            print("NURSE VISIT: She gives you an ice pack & calls home. Game over!")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
elif isClosed == "no":
    isPaper = input("Is there toilet paper in the stall? [yes/no] ")

    if isPaper == "yes":
        doorLocks = input("Does stall door lock? [yes/no] ")
        
        if doorLocks == "yes":
            print("PURE RELIEF: Working lock & paper!")
        elif doorLocks == "no":
            print("HOLD W/ FOOT: Door swings; make awkward eye contact with others!")
        else:
            print("Invalid Input")
    elif isPaper == "no":
        spareTowels = input("Spare towels or pass? [yes/no] ")

        if spareTowels == "yes":
            print("CRISIS AVERTED: Tough 1-ply saved ya.")
        elif spareTowels == "no":
            print("AIRDROP: Text a pal to slide supplies under the door!")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
