import json
from tinydb import TinyDB, Query
from model import player as play
from model import tournoi as tour
import operator

db = TinyDB('chess.json')


class Tournoi:

    NUMBER_OF_TOURS = 4
    matchs_list = []
    players_list = []

    def __init__(self, name, place, date):
        '''This is the class constructor'''

        self.name = name
        self.place = place
        self.date = date

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def time_control():
        # time control
        pass

    def add_comment():
        # write director's comment
        pass

    def save(self):
        '''This method serialize an instance of tournament and save it into a json file'''

        serialized_tournament = {'name': self.name,
                                 'place': self.place, 'date': self.date}
        tournaments_table = db.table('tournaments')
        tournaments_table.insert(serialized_tournament)
