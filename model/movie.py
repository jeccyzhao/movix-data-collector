import re 

class MovieItem(object):
    def __init__(self, id=None, imdb_id=None, tmdb_id=None, title=None, 
                year='', poster='', summary='', time='', rating=None, genres=None):
        self.id = int(id) if id else None
        self.imdb_id = int(imdb_id) if imdb_id else None
        self.tmdb_id = int(tmdb_id) if tmdb_id else None
        self.title = title
        self.poster = poster
        self.summary = summary
        self.time = time
        self.rating = float(rating) if rating else None
        self.genres = genres
        self.year = None
        self.init()

    @staticmethod
    def from_row(row):
        return MovieItem(id=row['id'], imdb_id=row['imdb_id'], 
                        tmdb_id=row['tmdb_id'], title=row['title'], 
                        year=row['year'], poster=row['poster'],
                        summary=row['summary'], time=row['time'], 
                        rating=row['rating']) if row else None

    def get_tuple_values(self):
        return (self.id, self.imdb_id, self.tmdb_id, self.title, self.year, self.poster, self.summary, self.time, self.rating)

    def init(self):
        match = re.match(r'.* \((\d+)\)', self.title)
        if match:
            self.year = int(match.group(1).strip())
            self.title = re.sub(r'\((.*)\)', "", self.title).strip()
    
    def __str__(self):
        return "id: {}, IMDB_ID: {}, Title: '{}', Year: {}, Rating: {}, Poster: '{}'".format(
            self.id, self.imdb_id, self.title, self.year, self.rating, self.poster)