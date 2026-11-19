import CaughtPokemon

print("Welcome to the Rotom Pokédex!")
menu = """ 
What would you like to do?
 "catch" - Log a newly caught Pokémon to the Pokédex
 "release" - Release a Pokémon from the Pokédex
 "change trainer" - Change the trainer name for future catches
 "print" - Display the current up to date list of all caught Pokémon
 "quit" - End the program
 \n\n\n\n\n\n
 """
trainer = input("What is your Trainer name? ")
party = []
ui = input(menu)

while ui != "quit":
    print("Welcome to the Pokédex,", trainer)
    # main loop
    if ui == "catch":
        pokemon_name = input("Which Pokémon did you catch? ")
        party.append(CaughtPokemon.CaughtPokemon(trainer, pokemon_name))
    elif ui == "print":
        for eachPoke in party:
            print(eachPoke)
    elif ui == "release":
        print("Which Pokémon would you like to release?")
        # show the Pokémon with IDs
        for eachPoke in party:
            print(eachPoke.get_dex_entry_id(), eachPoke)
        # get the id to delete
        idToRelease = int(input("id: "))
        # delete the id - with confirmation
        # find which entry has the id - then delete
        for i in range(len(party)):
            if party[i].get_dex_entry_id() == idToRelease:
                print(f"Entry\n{party.pop(i)} \nwas released into the wild!")
                break # literally it breaks the loop
    elif ui == "change trainer":
        trainer = input("What is your Trainer name? ")
    ui = input(menu)
