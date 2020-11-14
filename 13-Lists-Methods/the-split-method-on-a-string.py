user = "Bob,Dave,John,Sue,Randy,King"

print( user.split(sep= ',' ) )


## Using maxsplit 
# Limits the total number of splits
print( user.split(sep= ',' , maxsplit = 2) )


sentence = 'I'am learning how to code'
print(sentence.split(sep = ' '))