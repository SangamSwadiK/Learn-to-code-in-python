emp = ("Bob", "johnson", 'manager', 45)

# Doing this gives us too many values to unpack error
# first_name , last_name , details = emp


# So we do this

first_name , last_name , *details = emp

print(first_name, last_name, details)



*names, position, age = emp

print( names , position, age )


f1, *l1, age = emp

print( f1)
print( l1)
print( age )
