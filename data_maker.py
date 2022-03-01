from random import randint
from jina import DocumentArray
from docarray.document.generators import from_csv
from random import randint

with open("data/Movies.csv") as file:
    movies = DocumentArray(from_csv(file, field_resolver={'Summary': 'text'}))

movies = movies.shuffle(seed=randint)

for i in range(len(movies)):
    movies[i].text = movies[i].text  +  f"{ movies[i].tags['Genres'] }"  +  f"{ movies[i].tags['Title']}"

print(movies[0].text)
