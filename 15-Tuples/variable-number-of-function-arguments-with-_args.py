def accept_stuff( * args ):
    print('Type of args :: ', type(args))
    for arg in args:
        print( arg )

accept_stuff(1, 3, 4, 5)


def my_max(*numbers):
    g = numbers[0]

    for i in numbers:
        if i > g :
            g = i
    return g
print('***'*15)
print(my_max(1, 3))
print(my_max(1, 3, 9, 8, 8,656, 64, 8, 7))