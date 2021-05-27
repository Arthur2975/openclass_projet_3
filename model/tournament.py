from tinydb import TinyDB
from model.player import Player

db = TinyDB('chess.json')


class Tournament:

    def __init__(self, name, place, date,
                 number_of_tours=4, players=[], rounds=[],
                 time_control='bullet', comment=None):
        '''Class constructor'''

        self.name = name
        self.place = place
        self.date = date
        self.number_of_tours = number_of_tours
        self.players = players
        self.rounds = rounds
        self.time_control = time_control
        self.comment = comment

    def set_comment(self, comment):
        self.comment = comment

    def save(self):
        '''This method serialize an instance of tournament and save it into a json file'''

        serialized_tournament = {'name': self.name,
                                 'place': self.place, 'date': self.date, 'players': self.players,
                                 'rounds': self.rounds, 'number_of_tours': self.number_of_tours, }
        tournaments_table = db.table('tournaments')
        tournaments_table.insert(serialized_tournament)

    def load_tournament(tournament_number):
        tournament_table = db.table('tournaments')
        tournament_dict = tournament_table.all()
        tournament = tournament_dict[int(tournament_number)]
        tour = Tournament(name=tournament['name'], place=tournament['place'],
                          date=tournament['place'], players=tournament['players'], rounds=tournament['rounds'])
        return tour
