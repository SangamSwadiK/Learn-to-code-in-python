n = [4, 8, 15, 16, 0, -1]

def squares(n):
    squares = []
    for i in n:
        squares.append( i**2 )
    return squares
    
print( squares(n))



def cnvt_flot(n):
    res = []
    for i in n:
        res.append( float(i) )
    return res

print(cnvt_flot(n))


def e_or_o(n):
    res = []

    for i in n:
        if not i % 2:
            res.append(True)
        else:
            res.append(False)
    return res

print(e_or_o(n))