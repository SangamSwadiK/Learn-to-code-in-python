# A shallow copy works fine if lists are not nested !!

a = [1, 2, 3]

b = a[ : ]

print( a )
print( b )

print( a is b )


c = a.copy()

print( a )
print( c )
print( a is c )


import copy 

d = copy.copy( a )
print( a == d )
print( a is d)

print( '***'* 20)

numbers = [ 2, 3, 4]
a = [1, numbers, 5] 

b = a[ : ]
b = a.copy()
b = copy.copy( a )

print( a == b)
print( a is b)
print( a [1] is b[1] )

a[1].append( 100 )

print( b  )

########### DEEP COPY 

print('****'*25)

d = copy.deepcopy( a )

print( a == d)
print( a is d)
a[1].append('jajjaja')
print( a )
print( d )
print( a is d )  ### Deep copy internal items do not get modified



