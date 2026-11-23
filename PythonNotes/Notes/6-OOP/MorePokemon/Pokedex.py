# Pokedex.py

from Pokemon import Pokemon

pokedex = []

with open("PokedexData.csv", "r") as file:
    lines = file.readlines() # Returns a list of strings of lines

    for line in lines[1:]:
        components = line.rstrip().split(",")

        species = components[0]
        level = components[3]
        hp = components[4]
        moves = components[5:]

        pokedex.append(Pokemon(species, level, hp, moves))


for pokemon in pokedex:
    print(pokemon)