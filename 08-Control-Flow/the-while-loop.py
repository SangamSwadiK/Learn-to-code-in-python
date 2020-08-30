# Loop  : A series of  instructions that is repeated

count = 0
while count <= 5:
    # An infinite loop is one that never ends
    print(count)
    count += 1
    # So when count becomes 6 we come out of while loop

print('Careful, Count is :: ', count )

invalid_number = True

while invalid_number :
    user_value = int( input('Please enter a number above 10 :: ') )
    if user_value > 10 :
        print( f'Thanks, that works! {user_value} is a great choice')
        invalid_number = False
    else :
        print('You have entered an invalid number , try again')    
