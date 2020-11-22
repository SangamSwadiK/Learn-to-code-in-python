tv_shows  = {

    'The X files' : {
        'Season 1': {
            'Episodes' : 'Scary monster',
            'Genre': 'Actioon',
            'Year' : 1959
        },
        'Season 2' : {
            'Episodes' : 'Scary monster 2',
            'Genre': 'Comedy',
            'Year' : 1960
        }
    },

    'Lost' : {
        'Season 1': {
            'Episodes' : 'What ?',
            'Genre' : 'fantasy',
            'Year' : 2004
        }
    }
}


print( tv_shows['Lost'][ 'Season 1']['Genre'])