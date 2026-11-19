# SchrageCash.py

changeOwed = round(float(input("Changed Owed: ")), 2)

inQuarters = 0
inDimes    = 0
inNickles  = 0
inPennies  = 0

# Quarters, Dimes, Nickles, Pennies
coins = [0, 0, 0, 0]

postQuarters = changeOwed % 0.25
coins[0] = (changeOwed - postQuarters) // 0.25
print(coins[0])

postDimes = postQuarters % 0.1
coins[1] = (postQuarters - postDimes) // 0.1
print(coins[1])

postNickles = postDimes % 0.05
coins[2] = (postDimes - postNickles) // 0.05
print(coins[2])

coins[3] = postNickles // 0.01
print(coins[3])
