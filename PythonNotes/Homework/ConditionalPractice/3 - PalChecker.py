# PalChecker.py
integer = int(input("Enter a three-digit integer: "))

intString = str(abs(integer))
intPrinting = str(integer)
strLength = len(intString)

if strLength != 3:
    print(f"Error: {intString} is not 3-digit")
else:
    if intString[0] == intString[2]:
        print(f"{intPrinting} is a palindrome")
    else:
        print(f"{intPrinting} is not a palindrome")