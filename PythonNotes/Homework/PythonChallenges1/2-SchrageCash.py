# SchrageCash.py

changeOwed = round(float(input("Changed Owed: ")), 2) * 100

inQuarters = 0
inDimes    = 0
inNickles  = 0
inPennies  = 0

# Quarters, Dimes, Nickles, Pennies
coins = [0, 0, 0, 0]
names = ["Quarters", "Dimes", "Nickels", "Pennies"]

postQuarters = changeOwed % 25
coins[0] = (changeOwed - postQuarters) // 25

postDimes = postQuarters % 10
coins[1] = (postQuarters - postDimes) // 10

postNickles = postDimes % 5
coins[2] = (postDimes - postNickles) // 5

coins[3] = postNickles // 1

# Assign Correct Plurality
if coins[0] == 1:
    names[0] = "Quarter"
if coins[1] == 1:
    names[1] = "Dime"
if coins[2] == 1:
    names[2] = "Nickel"
if coins[3] == 1:
    names[3] = "Penny"

print(f"Out:")

for coin in range(len(coins)):
    if not (coins[coin] == 0):
        print(f"   {int(coins[coin])} {names[coin]}")