from tinydb import TinyDB
from model import player as play
from model import tournoi as tour

db = TinyDB('chess.json')


class Tournoi:

    def __init__(self, name, place, date, match=[], number_of_tours=4):
        '''Class constructor'''

        self.name = name
        self.place = place
        self.date = date
        self.match = match
        self.number_of_tours = number_of_tours

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
                                 'place': self.place, 'date': self.date, 'match': self.match, 'number_of_tours': self.number_of_tours, }
        tournaments_table = db.table('tournaments')
        tournaments_table.insert(serialized_tournament)

    def new_tournament():
        ''' This function creates a new tournament and save it into a json file'''

        new_tournament = tour.Tournoi(
            input(' New tournament: \n Tournament_s name '), input(' place '), input(' date '))
        tour.Tournoi.save(new_tournament)

    def new_player():
        '''This function creates a new player and save it into a json file'''

        continue_while = 0

        while continue_while == 0:
            add_player = input('Do you want to add a new player? : Y/N')
            if add_player.lower() != 'y':
                break
            else:
                new_player = play.Player(input('name: '), input('firstname: '), input(
                    'date_of_birth: '), input('gender: '), input('ranking: '))

            play.Player.save(new_player)
