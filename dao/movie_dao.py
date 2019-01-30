from model.movie import MovieItem
from common.constants import *

class MovieItemDAO(object):
    def __init__(self, conn):
        self.conn = conn
    
    def get_by_id(self, movie_id):
        items = []
        rows = self.conn.query("select * from t_movie where id = {}".format(movie_id))
        if rows and len(rows) > 0:
            for row in rows:
                items.append(MovieItem.from_row(row))
        return items

    def save_or_update(self, item):
        if item is not None:
            if len(self.get_by_id(item.id)) == 0:
                self.__add(item)
            else:
                self.__update(item)
        pass

    def __update(self, item):
        item.status = STAT_READY
        self.conn.execute("""update t_movie set id = %s, imdb_id = %s, tmdb_id = %s, title = %s, 
                year = %s, poster = %s, summary = %s, time = %s, rating = %s, status = %s where id = %s""", 
                item.get_tuple_values() + (item.id, ))
        print("Updated {}".format(item))

    def __add(self, item):
        item.status = STAT_NOT_READY
        self.conn.execute("""insert into t_movie (id, imdb_id, tmdb_id, title, year, poster, summary, time, rating, status)
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", item.get_tuple_values())
        print("Added {}".format(item))