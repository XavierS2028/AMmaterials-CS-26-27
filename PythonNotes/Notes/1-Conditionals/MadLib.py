# Ask User For Inputs

swallowType = input("What is your favorite type of swallow? ")
color = input("What is your favorite color? ")
treeType = input("What is your favorite type of tree? ")
iceCreamSeller = input("What is your favorite kind of animal? ")

petsName = input("What is your pet's name? ")
swallowSpeed = input(f"What is the air-speed velocity of an unladen {swallowType} swallow? (in miles per hour) ")

age = input(f"How old is {petsName.title()}? ")
flavor = input(f"What is your favorite ice cream flavor, {petsName.title()}? ")
rodentType = input("What is your favorite variety of rodent? ")

sandwichType = input("What is your favorite kind of sandwich? ")
favoriteMeal = input("What is your favorite meal of the day? ")
favoriteDrink = input("What is your favorite type of drink? ")

# Print Out Mad Lib
print(f"{petsName.title()} was just going to have a nice {sandwichType} sandwich and {favoriteDrink} for {favoriteMeal} on their {age} birthday.")
print(f"Suddenly, a wild {rodentType} appeared and stole {petsName.title()}'s sandwich!")
print(f"But, before the {rodentType} could eat the sandwich, an {swallowType} swallow swooped in and stole the sandwich again!")

print(f"The swallow swooped off and landed in a {treeType} tree.")
print(f"Feeling sad, {petsName.title()} walked off to buy some {flavor} ice cream from the nice {iceCreamSeller} down the street.")
print(f"The ice cream was {color} for some reason, but {petsName.title()} didn't care, it tasted good.")
print(f"Then, swooping in at {swallowSpeed} miles per hour, the swallow came back and decided to give {petsName.title()} back their sandwich.")
