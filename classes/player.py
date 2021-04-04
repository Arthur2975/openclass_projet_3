from tinydb import TinyDB
import json

db = TinyDB('chess.json')


class Player:
    '''Class defining a player and its attributes'''

    def __init__(self, name, firstname, date_of_birth, gender, ranking):
        '''This is the class constructor'''

        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

    def save(self):
        '''This method allows to serialize an instance and save it into a json file'''

        serialized_player = {'name': self.name, 'firstname': self.firstname,
                             'date_of_birth': self.date_of_birth, 'gender': self.gender, 'ranking': self.ranking}
        players_table = db.table('players')
        players_table.insert(serialized_player)

    # geter des infos joueur

    def get_ranking(self):
        return self.ranking

    def set_ranking(self, ranking):
        self.ranking = ranking
