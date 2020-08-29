empty_space = "            random gibberish asq      "

print( empty_space)

print( empty_space.rstrip() )
print( len(empty_space))
print( len(empty_space.rstrip()))


print( empty_space.lstrip() )
print( len(empty_space))
print( len(empty_space.lstrip()))


website = "www.python.org"
print( website.lstrip("w"))
print( website.rstrip('org'))
print(website.strip('worg'))   # Both sides
