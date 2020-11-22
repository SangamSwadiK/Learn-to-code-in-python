years = [1991, 1888, 1995, 2000, 1524]

## In dictionary when we use a pop it removes a key value pair

release_date = {
    'python' : 1991,
    'Ruby' : 1995,
    'Java' : 1995,
    'Go' : 2007
} 

print( release_date)
year = release_date.pop("Go")
print( year)


## For keys that do not exist, we get a default value ::
new = release_date.pop("Ruby", 2000)
print(new)