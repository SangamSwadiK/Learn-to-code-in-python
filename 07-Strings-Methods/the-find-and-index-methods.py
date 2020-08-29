# A method is a function that acts on a specific object.
# find returns the lowest index , if found else returns -1

city = "Bangalore"
print(city.find("B"))
print( city.find("galore") )

# If string is not found
print(city.find("Zzzz"))

print()
print(city.find('a', 2))
print( city.find(''))

print(city.index("galore"))

# If does not exist it gives a value error
#print( city.index('ZZZZzzz'))