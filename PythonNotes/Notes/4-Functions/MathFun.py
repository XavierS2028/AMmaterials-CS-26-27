import math

=== === === === === === === === === === === ===
# Pythagorean Theorem
def pythagorean(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

=== === === === === === === === === === === ===
# Distance Formula
def distance(x1, y1, x2, y2):
    return pythagorean((x2 - x1), (y2 - y1))

=== === === === === === === === === === === ===
# Linear Function
def linearFunc(xValue, slope, yIntercept):
    return slope * xValue + yIntercept

print(f"""
        x | y
        -----""")

for x in range(0, 11):
    print(f"\t{x} | {linearFunc(x, 2, 4)}")

=== === === === === === === === === === === ===
# Quadratic Formula
def quadratic(a, b, c):
    sqrtTerm = math.sqrt(b**2 - 4 * a * c)

    solution1 = (-b + sqrtTerm)/ (2 * a)
    solution2 = (-b - sqrtTerm)/ (2 * a)

    return (solution1, solution2)

=== === === === === === === === === === === ===
# Area of a Rectangle
def rectArea(width, height):
    return width * height

=== === === === === === === === === === === ===
# Volume of a Box
def boxVolume(length, width, height):
    return length * width * height

=== === === === === === === === === === === ===
# Integral Approximation of f(x)
def f(x):
    return x**2

x0 = 0
x1 = 4
n = 1000000
width = (x1 - x0) / n

area = 0
for i in range(n):
    x = x0 + i * width
    height = f(x)

    area += rectArea(height, width)

print(area)

=== === === === === === === === === === === ===
