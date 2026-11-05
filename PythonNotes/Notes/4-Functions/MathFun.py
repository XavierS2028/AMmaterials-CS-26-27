import math

def pythagorean(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

def distance(x1, y1, x2, y2):
    return pythagorean((x2 - x1), (y2 - y1))

def linearFunc(xValue, slope, yIntercept):
    return slope * xValue + yIntercept

def quadratic(a, b, c):
    sqrtTerm = math.sqrt(b**2 - 4 * a * c)

    solution1 = (-b + sqrtTerm)/ (2 * a)
    solution2 = (-b - sqrtTerm)/ (2 * a)

def rectArea(width, height):
    return width * height

def boxVolume(length, width, height):
    return length * width * height

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
