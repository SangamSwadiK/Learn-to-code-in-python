# Recursion : When A function calls itself.

def count_down_from( number ):
    while number >0:
        print( number )
        number -= 1
    
count_down_from( 4 )


# How can this be done with Recursion ??

print('***'*10)
def rec_count_down ( number ):
    if number <= 0:
        return
        
    print( number )
    rec_count_down ( number - 1 )

rec_count_down ( 5 )