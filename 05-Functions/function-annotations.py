# Python is a dynamic typed language
# Annotation is additional information about something

# no type checking is done here
def marks_multiplier( marks:int, times:float) -> float:
    return marks * times

print( marks_multiplier(15, 3))


print( marks_multiplier('Good morning ', 3))