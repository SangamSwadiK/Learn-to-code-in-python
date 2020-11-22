film_directors = {
    "Godfather" : "Francis ford Coppola",
    "The Rock" : "Micheal Bay",
    "Goodfella" : 'Martin Scorsese'
}

print( film_directors.get("Goodfella"))
print( film_directors.get("Aliens", 'NOTFOUND'))

film_directors.setdefault("Badboys")
print( film_directors)

film_directors.setdefault("Aliens", 'Director Not known')
print( film_directors)
