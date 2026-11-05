# XavUtils.py

def askQuestionYesNo(question: string, otherYes = [], otherNo = []):
    yesOptions = otherYes
    noOptions = otherNo

    yesOptions += ["yes", "y", "yeah"]
    noOptions += ["no", "n", "nah"]

    userResponse = input(question).lower()

    while not (userResponse in yesOptions or userResponse in noOptions):
        print("Error: Invalid response input: Reinput")

        userResponse = input(question).lower()

    if userResponse in yesOptions:
        return True
    elif userResponse in noOptions:
        return False

askQuestionYesNo("Do you want pizza? ")
