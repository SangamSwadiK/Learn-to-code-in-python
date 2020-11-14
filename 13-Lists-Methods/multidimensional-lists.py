food = [
    ['tomato', 'carrot', 'brinjal', 'potato'],
    ['dosa', 'chappati','parota','roti'],
    ['apple', 'banana', 'pineapple', 'grape']

]

# print( food)
# print(len(food))

print(food[0])
print(len(food[0]))


all_food = []

for f1 in food:
    for f2 in f1:
        all_food.append(f2)
print( all_food)