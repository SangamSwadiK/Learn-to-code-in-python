# A tuple is a fixed lenth list 
# A read only list !!!

foods = "Sushu", "Steak", "Guacamole"

foods = ( "Sushi", "Steak", "Guacamole")

print( type(foods))

empty = ()


print( type(empty))


mystery =  ( 1)
print( 'This wont be a TUPLE : ', mystery)

# Single tuple !!!
mystery  = ( 1, )
print( mystery )
print( type(mystery))

# or 

print( tuple([1]) ) 