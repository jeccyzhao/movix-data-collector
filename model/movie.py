import re 

class Movie(object):
    def __init__(self, id=None, imdb_id=None, tmdb_id=None, title=None, 
                year=None, poster=None, summary=None, time=None, rating=None, genres=None):
        self.id = id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id
        self.title = title
        self.poster = poster
        self.summary = summary
        self.time = time
        self.rating = rating
        self.genres = genres
        #self.year = None
        self.init()

    def init(self):
        match = re.match(r'.* \((.*)\)', self.title)
        if match:
            self.year = match.group(1).strip()
            self.title = re.sub(r'\((.*)\)', "", self.title).strip()
        else:
            print(self.title)
    
    def __str__(self):
        return "id: {}, IMDB_ID: {}, Title: '{}', Year: {}, Rating: {}, Poster: '{}'".format(
            self.id, self.imdb_id, self.title, self.year, self.rating, self.poster)