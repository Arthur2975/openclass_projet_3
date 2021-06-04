from tinydb import TinyDB

db = TinyDB('chess.json')


class Tournament:
    '''Defines a tournament and its attributes'''

    def __init__(self, name, place, date,
                 number_of_tours=4, players=[], players_i=[], number_of_players=8, rounds=[],
                 time_control='bullet', comment=None):

        self.name = name
        self.place = place
        self.date = date
        self.number_of_tours = number_of_tours
        self.number_of_players = number_of_players
        self.players = players
        self.players_i = players_i
        self.rounds = rounds
        self.time_control = time_control
        self.comment = comment

    def set_comment(self, comment):
        '''allow the tournament organizer to set a comment'''
        self.comment = comment

    def save(self):
        '''This method serialize an instance of tournament and save it into a json file'''

        serialized_tournament = {'name': self.name,
                                 'place': self.place, 'date': self.date,
                                 'players': self.players, 'players_i': self.players_i,
                                 'rounds': self.rounds, 'number_of_tours': self.number_of_tours,
                                 'number_of_players': self.number_of_players}
        tournaments_table = db.table('tournaments')
        tournaments_table.insert(serialized_tournament)

    def load_tournament(tournament):
        '''to load an instance of tournament from the db'''
        tour = Tournament(name=tournament['name'], place=tournament['place'],
                          date=tournament['place'], players=tournament['players'],
                          players_i=tournament['players_i'], rounds=tournament['rounds'])
        return tour
