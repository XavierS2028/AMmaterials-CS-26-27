#### Booleans ####
'''
True or False
    
if <condition>:
    <executeIfTrue>
elif <otherCondition>:
    <executeIfTrue>
else:
    <executeIfNoneAreTrue>
'''

import math

def CalculateRoots(a: int, b: int, c: int) -> (int, int):
   radical = math.sqrt(b**2 - 4*a*c)
   firstRoot = (-b + radical)/(2*a)
   secondRoot = (-b - radical)/(2*a)

   return (firstRoot, secondRoot)

roots = CalculateRoots(1, 0, 0)
print(f"First Root Is: {roots[0]}")
print(f"Second Root Is: {roots[1]}")

#### Logical Operators ####
'''
    >  - Greater Than
    <  - Less Than
    <= - Less Than Or Equal To
    >= - Greater Than Or Equal To
    == - Is Equal To
    != - Is Not Equal To

    is - Checks if memory addresses are the same

    and - Checks if both are true
    or  - Checks if either is true
'''

x = 10
y = 5

if x == y:
    print("X and Y are equal.")
else:
    print("X and Y are not equal.")

w = True
z = False

if w == z:
    print("W and Z are equal.")
elif w == (not z):
    print("W equals !Z")
