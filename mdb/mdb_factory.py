from mdb.impl.imdb_helper import ImdbHelper
from mdb.impl.tmdb_helper import TmdbHelper

class MDBFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def get_instance(type):
        return ImdbHelper() if type == "imdb" else TmdbHelper()
