from utils.imdb import ImdbHttpRequester
from dataset.parser import DatasetParser

if __name__ == "__main__":
    DatasetParser().get_movies()
    #print(ImdbHttpRequester().get_data(4046784))