# Pokedex.py

from Pokemon import Pokemon

pokedex = []

pokedex.append(Pokemon("Pikachu", "pika", 5, "electric", 400))
pokedex.append(Pokemon("Jolteon", "jolt", 4, "electric", 500))
pokedex.append(Pokemon("Umbreon", "um", 3, "dark", 600))
pokedex.append(Pokemon("Glaceon", "glace", 2, "ice", 700))

print(pokedex[0])
