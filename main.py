from dataset.parser import DatasetParser
from utils.db_helper import DatabaseConnection
from utils.imdb_helper import ImdbHelper
from dao.movie_dao import MovieItemDAO

DB_NAME = "movix"

if __name__ == "__main__":
    movies = DatasetParser().get_movies()
    if len(movies) > 0:
        ImdbHelper
        movie_dao = MovieItemDAO(DatabaseConnection(DB_NAME))
        for key, item in movies.items():
            movie_dao.save_or_update(ImdbHelper().enrich(item))
        #movie_dao.get_by_id(1)
    #print(ImdbHttpRequester().get_data(4046784))