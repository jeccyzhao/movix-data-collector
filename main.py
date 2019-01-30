from dataset.parser import DatasetParser
from utils.db_helper import DatabaseConnection
from mdb.mdb_factory import MDBFactory
from dao.movie_dao import MovieItemDAO
from common.constants import *

DB_NAME = "movix"

if __name__ == "__main__":
    movies = DatasetParser().get_movies()
    if len(movies) > 0:
        imdb_helper = MDBFactory.get_instance("imdb")
        tmdb_helper = MDBFactory.get_instance("tmdb")
        movie_dao = MovieItemDAO(DatabaseConnection(DB_NAME))
        for key, item in movies.items():
            movie = movie_dao.get_by_id(item.id)
            if len(movie) == 0 or movie[0].status == STAT_NOT_READY:
                item = tmdb_helper.enrich(imdb_helper.enrich(item))
                movie_dao.save_or_update(item)
        #movie_dao.get_by_id(1)
    #print(ImdbHttpRequester().get_data(4046784))