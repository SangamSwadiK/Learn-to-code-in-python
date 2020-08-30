# Elif condition to test another
# condition after the if statement


def positive_or_negative( number ):
    if number > 0 :
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else :
        return 'Number is Zero'

print( positive_or_negative( 0 ) )
print( positive_or_negative( 5 ) )
print( positive_or_negative( -89 ) )


def calculator( operation, a ,b):
    if operation =='add':
        return a + b
    elif operation =='subtract':
        return a - b
    elif operation =='multiply':
        return a * b
    elif operation =='divide':
        return a / b
    # Else statement is not mandatory!!

print( calculator('add', 1, 1))
print(calculator ('ajhahysyysy', 5 , 5))  # Ahah


def calculator2( operation, a ,b):
    if operation =='add':
        return a + b
    elif operation =='subtract':
        return a - b
    elif operation =='multiply':
        return a * b
    elif operation =='divide':
        return a / b
    else :
        return (' operation not available')
    # Else statement is not mandatory!!

print( calculator2('add', 1, 1))
print(calculator2 ('ajhahysyysy', 5 , 5)) # Now it works
