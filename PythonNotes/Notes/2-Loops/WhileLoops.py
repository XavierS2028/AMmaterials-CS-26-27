#### WHILE LOOPS ####
# While boolean expression is true, do something.

import string

i = 0
while(i < 10):
    print(i, end=", ")
    i += 1

print()

i = 9
while(i >= 0):
    print(i, end=", ")
    i -= 1

print()

i = -10
while i <= 10:
    print(i, end=", ")
    i += 1

print()

i = 0
while i <= 10:
    print(i, end=", ")
    i += 2

print()

i = 1
while i < 10:
    print(i, end=", ")
    i += 2

print()

i = -100
while i <= 100:
    print(i, end=", ")
    i += 20

print()

for char in string.ascii_uppercase:
    print(char, end=", ")
