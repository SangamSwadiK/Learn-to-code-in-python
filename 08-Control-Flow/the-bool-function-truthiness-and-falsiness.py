# Truthiness and falsiness

# 0 is a falsy value and any other number is truthy value
if 3:
    print('Hello')

if -1 :
    print('Truthy value')

if 0:
    print('Falsy value')

if 'Hello':
    print('Aahahahhahaha')

if ' ':
    print('hmmmm')

if '':
    print('??????????')

print( bool(-1) )
print( bool(0) )
print( bool('Bangalore') )
print( bool('') )
print( bool(-1.35684565) )
print( bool(0.0) )