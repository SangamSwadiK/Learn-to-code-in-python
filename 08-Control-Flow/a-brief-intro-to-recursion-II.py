def wh_reverse (string):

    start_ind = 0
    last_ind = len(string) - 1 
    reversed_string = ''
    while last_ind >= start_ind :
        reversed_string += string[last_ind]
        last_ind -= 1

    print( reversed_string)

wh_reverse( 'straw')



# def reverse ( string, new_string = '' ):
#     new_string += string
#     if len(string) == 0:
#         return 
#     print( string[ -1 ] )
#     reverse ( string[ :-1 ])


def rev ( string ):
    if len( string ) <= 1:
        return string
    
    return string[-1] + rev( string [ 0 : -1] )

print( rev('straw') )
# straw
# w + rev(stra)
# w + a + reverse( str )
# w + a + r + rev( st )
# w + a + r + t + s





print( reverse('straw'))  # warts