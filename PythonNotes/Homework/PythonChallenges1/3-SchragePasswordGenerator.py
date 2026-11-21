# SchragePasswordGenerator.py

import string
import random

specialCharacters = "!@#$%^&*()"

# I just yoinked this function from a previous assignment
def askQuestionYesNo(question:string) -> bool:
    yesOptions = ["yes", "y", "yeah"]
    noOptions  = ["no", "n", "nah"]

    userResponse = input(question).lower()

    while not (userResponse in yesOptions or userResponse in noOptions):
        print("Error: Invalid response input: Reinput")

        userResponse = input(question).lower()

    if userResponse in yesOptions:
        return True
    elif userResponse in noOptions:
        return False

# Should be a list of format [capitalsLeft, lowersLeft, numbersLeft, specialsLeft]
def pickRandomCharType(charsLeft) -> int:
    randType = random.randint(0, 3)

    while charsLeft[randType] == 0:
        randType = random.randint(0, 3)

    return randType

while askQuestionYesNo("Generate a password? (y/n): "):
    numCapitals = int(input("How many capital letters do you want in your password? "))
    numLowers   = int(input("How many lowercase letters do you want in your password? "))
    numNumbers  = int(input("How many numbers do you want in your password? "))
    numSpecials = int(input("How many special characters do you want in your password? "))

    passwordString = ""

    for character in range(numCapitals + numLowers + numNumbers + numSpecials):
        charType = pickRandomCharType([numCapitals, numLowers, numNumbers, numSpecials])

        if charType == 0:
            passwordString += chr(random.randint(65, 90))  # A-Z
            numCapitals -= 1
        elif charType == 1:
            passwordString += chr(random.randint(97, 122)) # a-z
            numLowers -= 1
        elif charType == 2:
            passwordString += chr(random.randint(48, 57))  # 0-9
            numNumbers -= 1
        else:
            passwordString += specialCharacters[random.randint(0, len(specialCharacters) - 1)]
            numSpecials -= 1

    print(f"Password: {passwordString}")