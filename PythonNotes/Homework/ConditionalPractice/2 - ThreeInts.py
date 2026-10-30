#ThreeInts.py
a = int(input("Input the first integer: "))
b = int(input("Input the second integer: "))
c = int(input("Input the third integer: "))

smallestInt = a
middleInt   = b
largestInt  = c

if a >= b and a >= c:
    # A is the largest
    largestInt = a
    if b >= c:
        # C is smallest
        middleInt = b
        smallestInt = c
    else:
        # B is smallest
        middleInt = c
        smallestInt = b

elif b >=a and b >=c:
    # B is the largest
    largestInt = b
    if a >= c:
        # C is smallest
        middleInt = a
        smallestInt = c
    else:
        # A is smallest
        middleInt = c
        smallestInt = a

else:
    # C is the largest
    largestInt = c
    if a >= b:
        # B is smallest
        middleInt = a
        smallestInt = b
    else:
        # A is smallest
        middleInt = b
        smallestInt = a

print(f"Numbers in ascending order are: {smallestInt}, {middleInt}, {largestInt}")