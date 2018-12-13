from collections import defaultdict, namedtuple, Counter, deque
import csv

movies_csv = 'movies.csv'

Movie = namedtuple('Movie', 'director title year score')

def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            
            m = Movie(director=director, title=movie, year=year, score=score)
            directors[director].append(m)
    return directors

directors = get_movies_by_director()

#print(directors['Woody Allen'])

def get_movies_by_year(data=movies_csv):
    movies = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            
            m = Movie(director=director, title=movie, year=year, score=score)
            movies[year].append(m)
    return movies

movies = get_movies_by_year()

year = input('What year would you like to see movies from?')

year = int(year)

print(movies[year])