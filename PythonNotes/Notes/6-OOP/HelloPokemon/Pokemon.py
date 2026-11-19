# Pokemon.py

# imports
# define class
#   define public member variables
#   define constructor
#   define getters and setters
#   define methods
#   define toString

class Pokemon:
    def __init__(self, species, nickname, level, pType, hp):
        self.nickname = nickname.title()
        self.species = species.title()
        self.level = level
        self.pType = pType.title()
        self.hp = hp

    def __str__(self):
        output = f"{self.species}\n   {self.nickname}\n   Level: {self.level}"
        return output

    #### Methods ####
    def evolve(self, newSpecies: string):
        self.species = newSpecies.title()

    def takeDamage(self, damage: int):
        self.hp -= damage

    #### Getters and Setters ####
    def setSpecies(self, species: string):
        self.species = species.title()
    def getSpecies(self) -> string:
        return self.species

    def setNickname(self, nickname: string):
        self.nickname = nickname.title()
    def getNickname(self) -> string:
        return self.nickname

    def setLevel(self, level: int):
        if level > 0:
            self.level = level
        else:
            self.level = 0
    def getLevel(self):
        return self.level
