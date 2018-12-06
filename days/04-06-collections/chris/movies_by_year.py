# This little project will show you a sorted by rating
# list of movies that was released in a given year

from collections import defaultdict, namedtuple, Counter
import csv

Movie = namedtuple('Movie','title, rating')

years_of_movies = defaultdict(list)

with open('movie_metadata.csv', encoding='utf-8') as f:
    movies_csv = csv.DictReader(f)
    for row in movies_csv:
        movie = Movie(title=row['movie_title'],rating=row['imdb_score'])
        years_of_movies[row['title_year']].append(movie)
    
def get_movies_by_year(year):
    print(f'Here are all the movies released in {year} sorted by rating:',end='\n\n')
    # I actually don't know what lambda functions are, but this is a method I found
    # to sort named tuples by one of their values
    sorted_movies = sorted(years_of_movies[year], key=lambda x: x.rating, reverse=True)
    for movie in sorted_movies:
        print(f'{movie.title} was rated {movie.rating}')

input_year = input('What year of movies do you want to fetch? ')
get_movies_by_year(input_year)