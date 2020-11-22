birthday = ( 4, 12, 1991)
print( len(birthday))

print(birthday[0])
print(birthday[1])
print(birthday[2])

# Gives index error 
# print(birthday[120]) # Gives an error !

# Tuple wont support assignment
# birthday[1] = 12

# The tuple can contain mutable objects within it !!

addresses = (
    ["Hudson Street", "New York", "NY"],
    ['Franklin St', 'San Francisco', 'CA']
            )


# Cant do this
# addresses[1] = ['balh ,balh', 'ahah']
# print(addresses)

# But we can do this
addresses[0][1] = 'jja jaja'
print(addresses)