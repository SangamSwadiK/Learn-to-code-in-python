# Default Arguments : Fallback arguments that  are passed to the function 
# if an explicit value is not provided to the parameter.

def add(a=1, b=1):
    return a + b

print(add(7, 8))
print(add(12))
print(add())