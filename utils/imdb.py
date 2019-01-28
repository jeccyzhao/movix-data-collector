import requests
from common.constants import *
from bs4 import BeautifulSoup
from model.movie import Movie

class ImdbHttpRequester(object):
    def __init__(self, host=IMDB_HOST, proxy=PROXY):
        self.host = host
        self.proxies = self.get_proxies(proxy)
    
    def get_url(self, imdb_id):
        return "{}/title/{}".format(self.host, IMDB_TT_PREFIX + str(imdb_id).zfill(IMDB_ID_MAXIMUM_SIZE))

    def get_proxies(self, proxy):
        return {"http": proxy, "https": proxy} if proxy is not None else {}

    def __get_poster(self, soup):
        el = soup.select(".poster a img")
        return el[0]['src'] if len(el) > 0 else None

    def __get_summary(self, soup):
        el = soup.select(".summary_text")
        return el[0].get_text() if len(el) > 0 else None

    def __get_duration(self, soup):
        el = soup.select(".subtext time[datetime]")
        return el[0].get_text().strip() if len(el) > 0 else None

    def __get_rating(self, soup):
        el = soup.select(".ratingValue strong span")
        return el[0].get_text().strip() if len(el) > 0 else None

    def get_data(self, imdb_id):
        res = requests.get(self.get_url(imdb_id), proxies=self.proxies)
        if res.status_code is not 200:
            print("Failed to get remote file, code: " + str(res.status_code) + " reason: " + res.reason)
            return None
        soup = BeautifulSoup(res.text, features="html.parser")
        return Movie(imdb_id=imdb_id,
                    summary=self.__get_summary(soup),
                    poster=self.__get_poster(soup),
                    duration=self.__get_duration(soup),
                    rating=self.__get_rating(soup))
