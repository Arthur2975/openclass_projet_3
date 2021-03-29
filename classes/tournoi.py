from tinydb import TinyDB
import json

db = TinyDB('chess.json')

class Tournoi:

    NUMBER_OF_TOURS = 4
    matchs_list = []
    players_list = []


    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def time_control():
        #time control
        pass

    def add_comment():
        #write director's comment
        pass

    def save(self):
        serialized_tournament = {'name': self.name, 'place': self.place, 'date': self.date}
        tournaments_table = db.table('tournaments')
        tournaments_table.insert(serialized_tournament)

    def save_json(self):
        serialized_tournament = {'name': self.name, 'place': self.place, 'date': self.date}
        with open('chess.json', 'w') as json_file:
            js = json.dump(serialized_tournament, json_file)


