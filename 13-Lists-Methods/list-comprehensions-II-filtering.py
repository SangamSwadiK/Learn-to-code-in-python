print(['abcdefghijklmnopqrstuvwxyz'.index(char) for char in "donut"])

print([ number/ 2 for number in range(20)])


donuts = ['Jelly', 'Chocolate', 'Glazed', 'Boston Cream', 'Vanilla Cream']

creamy_donuts = [  donut for donut in donuts if 'Cream' in donut]
print(creamy_donuts)