#### Challenge 1 ####
'''
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
'''      
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
'''
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
'''
#### Challenge 4 ####

#### Challenge 5 ####

