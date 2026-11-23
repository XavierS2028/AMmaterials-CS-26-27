# Pokemon.py

import string

class Pokemon:
    def __init__(self, species: string, level: int , hp: int, moves: list[string]):
        self.species = species
        self.level = level
        self.hp = hp
        self.moves = moves

    def getMoves(self) -> list[string]:
        return self.moves

    def setSpecies(self, species: string):
        self.species = species.title()

    def __str__(self) -> string:
        output = f"{self.species}\n   Level: {self.level}\n   HP: {self.hp}\n"
        output += "   Moves:\n"

        for move in self.moves:
            output += f"    - {move}\n"

        return output
