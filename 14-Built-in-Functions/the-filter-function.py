animals = ['elephant', 'horse', 'cheetah', 'dog', 'fish']
long_words = [ animal for animal in animals if len(animal)> 5 ]

def is_long_animal(animal):
    return len(animal) > 5

print( long_words )

# function has to return a boolean
print('Filter res ::', list(filter(is_long_animal, animals)))