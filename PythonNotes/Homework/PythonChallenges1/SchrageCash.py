# SchrageCash.py

changeOwed = round(float(input("Changed Owed: ")), 2)

quarterCount = 0
dimeCount = 0
nickleCount = 0
pennyCount = 0

for i in range(0, changeOwed, 0.25):
    quarterCount += 1

changeOwed -= quarterCount * 0.25

for i in range(0, changeOwed, 0.1):
    dimeCount += 1

changeOwed -= dimeCount * 0.1

for i in range(0, changeOwed, 0.05):
    nickleCount += 1

changeOwed -= nickleCount * 0.05

for i in range(0, changeOwed, 0.01):
    pennyCount += 1

changeOwed -= pennyCount * 0.01

print(f"Change Owed: ${changeOwed:.2f}")
print(f"\tQuarters: {quarterCount}")
print(f"\tDimes: {dimeCount}")
print(f"\tNickles: {nickleCount}")
print(f"\tPennies: {pennyCount}")