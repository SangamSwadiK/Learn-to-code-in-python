pokemon = {

    "Fire" : ["Charmander", "Charmeleon", "Charizard"],
    "Water" : ["Squirtle", "Warturtle", "Blastoise"],
    "Grass" : ["Bulbasaur", "Venusaur", "Ivysaur"]        
}

print( "Fire" in pokemon)
print( "Grass" in pokemon)
print( "Electric" in pokemon)

print( "Fire" not in pokemon)
print( "Grass" not in pokemon)
print( "Electric" not in pokemon)

if "Zombie" in pokemon:
    print( pokemon['Zombie'] )
else:
    print('The category of Zom')
