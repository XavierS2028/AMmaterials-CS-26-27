# CaughtPokemon.py

from datetime import datetime

class CaughtPokemon:
    dexID = 1

    def __init__(self, trainerName, pokemonName):
       self.trainerName = trainerName
       self.pokemonName = pokemonName
       self.id = CaughtPokemon.dexID
       CaughtPokemon.dexID += 1
       self.timestamp = datetime.now()

    def __str__(self):
        output = f"{self.trainerName} caught {self.pokemonName}"
        output += f"\n\tCaught at timestamp: {self.timestamp}"
        return output

    def get_dex_entry_id(self):
        return self.id 
