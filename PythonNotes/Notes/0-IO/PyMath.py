import math
import cmath

# Problem 1
print("Problem 1:")
print(8*(1/3)*68)

# Problem 2
print("Problem 2:")
print(8*(14)*((2/81)/(3/7)))

# Problem 3
print("Problem 3:")
print(math.pow(2, 2) + math.pow(14, 2))

# Problem 4
print("Problem 4:")
print(math.sqrt(math.pow(6.5,2) + math.pow(-3-2/3, 2)))

#### Division ####
print(7/3)   # returns a float
print(7//3)  # returns an int. Truncates the decimal

#### Modulus ####
print(7%3)   # returns the remainder of 7/3

#### Finding Roots ####
a = 2
b = 4
c = -7

root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print(f"Roots Are: {round(root1, 3)} and {root2:.3f}")

#### Complex Math ####
print(cmath.sqrt(-4))
print(cmath.sqrt(j))

#### Evaluation ####
# eval()  evaluates a string
# int()   converts a string to an integer
# float() converts a string to a float
# str()   converts another type to a string
# bool()  converts a string or int to a bool

<= >= /= != ==
