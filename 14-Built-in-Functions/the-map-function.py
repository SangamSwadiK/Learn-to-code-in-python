numbers = [1, 4, 8, 15, 16, 23, 42]
cubes = [ number ** 3 for number in numbers ]
print( cubes )

def cube(number):
    return number**3

print('Map result :: ',  list(map(cube, numbers) ) )



animals = ['Cat', 'Bear', 'cheetah', 'fish']

print( 'Length from map :: ',  list(map( len, animals ) ) )