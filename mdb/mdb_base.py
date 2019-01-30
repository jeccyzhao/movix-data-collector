from common.constants import *
import requests
from model.movie import MovieItem
from bs4 import BeautifulSoup
from common.constants import *

class MDBHelper(object):
    def __init__(self, host, proxy=PROXY):
        self.host = host
        self.proxies = self.get_proxies(proxy)
    
    def get_url(self, id):
        raise NotImplementedError("Function is not implemented")
    
    def get_proxies(self, proxy):
        return {"http": proxy, "https": proxy} if proxy is not None else {}
    
    def _get_poster(self, soup):
        raise NotImplementedError("Function is not implemented")
    
    def _get_summary(self, soup):
       raise NotImplementedError("Function is not implemented")
    
    def _get_rating(self, soup):
        raise NotImplementedError("Function is not implemented")
    
    def _get_time(self, soup):
        raise NotImplementedError("Function is not implemented")
    
    def _get_id(self, movie):
        raise NotImplementedError("Function is not implemented")

    def get_data(self, id):
        url = self.get_url(id)
        print("Fetching movie data from {}".format(url))
        res = requests.get(url, proxies=self.proxies)
        if res.status_code is not 200:
            print("Failed to get remote file, code: " + str(res.status_code) + " reason: " + res.reason)
            return None
        soup = BeautifulSoup(res.text, features="html.parser")
        return MovieItem(summary=self._get_summary(soup),
                        poster=self._get_poster(soup),
                        time=self._get_time(soup),
                        rating=self._get_rating(soup))
    
    def enrich(self, movie):
        if movie is not None:
            data = self.get_data(self._get_id(movie))
            if data is not None:
                movie.summary = data.summary if data.summary is not None else movie.summary
                movie.poster = data.poster if data.poster is not None else movie.poster
                movie.time = data.time if data.time is not None else movie.time
                movie.rating = data.rating if data.rating is not None else movie.rating
        return movie 