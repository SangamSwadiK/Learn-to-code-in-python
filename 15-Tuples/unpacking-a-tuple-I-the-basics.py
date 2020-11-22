emp = ("Bob", "johnson", 'manager', 45)

first_name = emp[0]
last_name = emp[1]
age = emp[2]


print(first_name, last_name, age )


# Alternative to the above 
# We now do this !!

f_name, s_name, age = emp

print(f_name, s_name, age)

# Too many values to unpack error ( Value error )
# a, b = emp

a = 5
b = 10
print('before :: ',  a , b)
b, a = a, b
print( 'After :: ', a , b)