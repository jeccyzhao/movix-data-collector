from common.constants import *
from model.movie import MovieItem
from mdb.mdb_base import MDBHelper

class TmdbHelper(MDBHelper):
    def __init__(self, host=TMDB_HOST, proxy=PROXY):
        super(TmdbHelper, self).__init__(host, proxy)

    def get_url(self, id):
        return "{}/{}".format(self.host, str(id))
    
    def _get_poster(self, soup):
        el = soup.select(".poster .image_content img")
        return el[0]['src'] if len(el) > 0 else None
    
    def _get_summary(self, soup):
        el = soup.select(".overview p")
        return el[0].get_text() if len(el) > 0 else None
    
    def _get_time(self, soup):
        return None

    def _get_rating(self, soup):
        return None
    
    def _get_id(self, movie):
        return movie.tmdb_id if movie is not None else None
    