# userInput = input("Hey, guess what? ").lower()

# while userInput != "wsp":
#     userInput = input("Hey, guess what? ").lower()
# print("Chicken Butt")

secretNumber = 7
userGuess = int(input("Guess a number between 1 and 10: "))

while(userGuess != secretNumber):
    if userGuess > secretNumber:
        print("Too high")
    else:
        print("Too low")

    userGuess = int(input("Guess a number between 1 and 10: "))

print("You guessed right!")
