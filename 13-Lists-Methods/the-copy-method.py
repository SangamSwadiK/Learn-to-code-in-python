units = ['meter', 'candela', 'mole', 'second', 'ampere']

more_units = units.copy()

print( units )
print( more_units)

print('****'* 15)

units.remove('candela')
print(units)
print(more_units)

print('****'* 15)

# another  syntax for making a copy is [ : ]