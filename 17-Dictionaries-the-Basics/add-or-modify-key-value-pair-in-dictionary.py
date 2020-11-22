sports_team = { "Bangalre" : "RCB", "Mumbai" : 'Mumbai Indians'}


print( sports_team )

sports_team [ 'Kolkata'] = 'Knight Riders'

print( sports_team)

video_game_options = {}
video_game_options  = dict()

video_game_options [ "Subtitles"] = True
video_game_options ['difficulty'] = 'Medium'

video_game_options ['volume'] = 7
print( video_game_options )



words = ['danger', 'beware', 'danger']

def count_words( words ):
    counts = {}
    for word in words :
        if word in counts.keys() :
            counts[word] += 1
        else :
            counts[ word ] = 1
    return counts 

print( count_words (words))




