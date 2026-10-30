# Distances.py

import math

x1 = int(input("Enter the first x coordinate: "))
y1 = int(input("Enter the first y coordinate: "))
x2 = int(input("Enter the second x coordinate: "))
y2 = int(input("Enter the second y coordinate: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.3f}")