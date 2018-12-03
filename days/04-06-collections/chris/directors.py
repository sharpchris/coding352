from collections import defaultdict, namedtuple, Counter
import csv

# Name Tuple
Movie = namedtuple('Movie','title, rating')

# Default Dict
directors_with_movies = defaultdict(list)

# The Pythonic way of opening a file is to use a context manager ("with")
with open("movie_metadata.csv", encoding='utf-8') as f:
    movies_csv = csv.DictReader(f)
    for row in movies_csv:
        # Build a dictionary with director names as the key, and the
        # movies they directed as a list of named tuples
        movie = Movie(title=row['movie_title'],rating=row['imdb_score'])
        directors_with_movies[row['director_name']].append(movie)

    # Now I can get all the movies that was directed by an individual
    print(directors_with_movies['Ridley Scott'],end='\n\n')

# Now let's use a Counter to make it easier to work with the data
c = Counter()
# director_with_moviews is a dictionary, so there are two items
# calling it by 'director, movies' in the dictionary helps me
# because I can give a friendly name to the key and value, the value
# beeing a list of named tuples in this case
for director, movies in directors_with_movies.items():
    c[director] += len(movies)

print(c.most_common(5))
# Without data cleaning, the most common director is: ''
# haha

