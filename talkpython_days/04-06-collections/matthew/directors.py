from collections import defaultdict, namedtuple, Counter
import csv


Movie = namedtuple('Movie', 'title, year, rating')

# set up our dictionary
directors = defaultdict(list);

with open('movie_metadata.csv', encoding='utf-8') as f:
    movies_csv = csv.DictReader(f)
    for row in movies_csv:
        movie = Movie(title=row['movie_title'], year=row['title_year'], rating=row['imdb_score'])
# append movies info to the dictionary
        directors[row['director_name']].append(movie)
# print it out though the '\n\n' part doesn't do anything for me
    print(directors['Woody Allen'], end='\n\n')

ctr = Counter()

# loop through the directors
for director, movies in directors.items():
    ctr[director] += len(movies)

print(ctr.most_common(5))