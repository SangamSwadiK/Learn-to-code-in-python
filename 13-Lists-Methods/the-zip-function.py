# Zip function

breakfast = ['eggs', 'cereal', 'banana']
lunches = ['sushi', 'chicken teriyaki', 'Soup']
dinners = ['Steak', 'Meatballs', 'Pasta']

print(zip(breakfast, lunches, dinners))

print(type(zip(breakfast, lunches, dinners)) )

# print( list(zip(breakfast, lunches, dinners)) )

for  breakfast, lunch, dinner in zip(breakfast, lunches, dinners):
    print( breakfast, lunch, dinner)