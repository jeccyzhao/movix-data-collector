import csv
from model.movie import MovieItem
from common.constants import *

class DatasetParser(object):
    def __init__(self):
        pass

    def get_movies(self):
        movies = self.__parse_movies()
        if len(movies) > 0:
            self.__parse_links(movies)
        return movies

    def __get_dataset_file(self, file):
        return "dataset/{}".format(file)

    def __get_csv(self, file):
        f = open(self.__get_dataset_file(file), encoding='utf-8')
        return csv.reader(f)

    def __parse_tags(self, movies, file=DS_FILE_TAGS):
        pass
    
    def __parse_links(self, movies, file=DS_FILE_LINKS):
        fcsv = self.__get_csv(file)
        headers = next(fcsv)
        for row in fcsv:
            movie_id = row[0]
            if movie_id in movies:
                movies[movie_id].imdb_id = int(row[1]) if row[1] else None
                movies[movie_id].tmdb_id = int(row[2]) if row[2] else None
    
    def __parse_movies(self, file=DS_FILE_MOVIE):
        movies = {}
        fcsv = self.__get_csv(file)
        headers = next(fcsv)
        for row in fcsv:
            movie_id = row[0]
            movies[movie_id] = MovieItem(id=movie_id, title=row[1], genres=row[2])
        return movies