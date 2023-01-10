import spacy

# load spacy medium language model, declare global variables.
nlp = spacy.load('en_core_web_md')
movie_choices = {}
similarity_list = []


# function takes last watched movie description as a parameter and returns name of most similar movie.
def watch_next(watched_movie):
    movie_description = list(movie_choices.keys())
    movie_name = list(movie_choices.values())

    for description in movie_description:
        similarity_list.append(nlp(description).similarity(nlp(watched_movie)))

    most_similar = similarity_list.index(max(similarity_list))
    return movie_name[most_similar]


# read in movies.txt file.
with open("movies.txt", "r") as f:
    movies = f.readlines()

# update movie choices, with movie descriptions as keys and movie names as values.
for movie in movies:
    movie_choices.update({movie.strip().split(" :")[1]: movie.strip().split(" :")[0]})


# utilised multiline string for readability/presentation.
# the difference in similarity using multi-line string vs. single line was statistically insignificant.
planet_hulk = '''
Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.
'''

next_movie = watch_next(planet_hulk)
print(f"The next movie you should watch is: {next_movie}")
