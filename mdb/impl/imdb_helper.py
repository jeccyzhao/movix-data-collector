from common.constants import *
from model.movie import MovieItem
from mdb.mdb_base import MDBHelper

class ImdbHelper(MDBHelper):
    def __init__(self, host=IMDB_HOST, proxy=PROXY):
        super(ImdbHelper, self).__init__(host, proxy)
    
    def get_url(self, id):
        return "{}/title/{}".format(self.host, IMDB_TT_PREFIX + str(id).zfill(IMDB_ID_MAXIMUM_SIZE))

    def _get_poster(self, soup):
        el = soup.select(".poster a img")
        return el[0]['src'] if len(el) > 0 else None

    def _get_summary(self, soup):
        el = soup.select(".summary_text")
        return el[0].get_text() if len(el) > 0 else None

    def _get_time(self, soup):
        el = soup.select(".subtext time[datetime]")
        return el[0].get_text().strip() if len(el) > 0 else None

    def _get_rating(self, soup):
        el = soup.select(".ratingValue strong span")
        return el[0].get_text().strip() if len(el) > 0 else None
    
    def _get_id(self, movie):
        return movie.imdb_id if movie is not None else None