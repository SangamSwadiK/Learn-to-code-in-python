# Multiple conditions
if 5 < 7 and "rain"=='rain':
    print( 'This Evaluates to True')

if  'rain' == 'fire' and 5 < 7:
    print(" This will not print because at least one of them is false")

value = 95 

if value > 90 and value < 100 :
    print( 'Value lies between 90 and 100')

if 90 < value < 100:# Bypasses the and syntax

    print( 'Lies between 90 and 100')


