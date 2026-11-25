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


def getPokemonIndexFromInput() -> int:
    userInput = input("What pokemon do you want to view? ").rstrip().title()

    pokemonSpecies = []

    for pokemon in pokedex:
        pokemonSpecies.append(pokemon.species)

    if userInput in pokemonSpecies:
        return pokemonSpecies.index(userInput)
    else:
        return -1

pokemonIndex = getPokemonIndexFromInput()

if not pokemonIndex == -1:
    pokemon = pokedex[pokemonIndex]

    print(f"""{pokemon.level} {pokemon.species} has the following attacks:""")
    for move in pokemon.moves:
        print(f"   {move}")
