from tinydb import TinyDB
from model.tournament import Tournament
from views.views import Views
from model.round import Round
from model.player import Player

db = TinyDB('chess.json')


class Report:
    '''Docstring'''

    def __init__(self):
        pass

    def report_all_actors(self):
        actors_table = db.table('players')
        all_actors = actors_table.all()
        print(all_actors)

    def report_all_players(self):
        players_table = db.table('players')
        all_players = players_table.all()
        for player in all_players:
            print('--------------------------------------------')
            print('name: ' + str(player['name']) + ', firstname: ' +
                  str(player['firstname']) + ', ranking: ' + str(player['ranking']))

    def report_all_tournaments(self):
        tournaments_table = db.table('tournaments')
        all_tournaments = tournaments_table.all()
        for tournament in all_tournaments:
            print('------------')
            print('name: ' + str(tournament['name']) + ', place: ' +
                  str(tournament['place']) + ', date: ' + str(tournament['date']))

    def report_all_rounds(self):
        rounds_table = db.table('rounds')
        rounds = rounds_table.all()
        for round in rounds:
            print('-------------')
            print('name: ' + str(round['name']), 'matchs: ' + str(round['match_list']))

    def report_all_match(self):
        pass
