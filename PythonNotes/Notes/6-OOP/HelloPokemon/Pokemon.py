# Pokemon.py

'''
Classes and Objects
    
'''

# imports
# define class
#   define public member variables
#   define constructor
#   define getters and setters
#   define methods
#   define toString

class Pokemon:
    def __init__(self, species, nickname, level, pType, hp):
        self.nickname = nickname
        self.species = species
        self.level = level
        self.pType = pType
        self.hp = hp

    def setSpecies(self, species: string):
        self.species = species.title()
    def getSpecies(self) -> string:
        return self.species

    def setNickname(self, nickname: string):
        self.nickname = nickname.title()
    def getNickname(self) -> string:
        return self.nickname.title()

pikachu = Pokemon("Pikachu", "tim", 5, "pokemon", 500)
pikachu.setSpecies("banana")
print(pikachu.getNickname())
