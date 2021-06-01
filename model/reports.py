from tinydb import TinyDB
from operator import itemgetter
from views.views import Views

db = TinyDB('chess.json')


class Report:
    '''Docstring'''

    def __init__(self):
        pass

    def report_all_actors(self):
        actors_table = db.table('players')
        all_actors = actors_table.all()
        user_answer = Views.sorted_report()
        if user_answer == 1:
            sorted_actors = sorted(all_actors, key=itemgetter('name'), )
            for actor in sorted_actors:
                print('name: ' + str(actor['name']) + ' Firstname: ' +
                      str(actor['firstname']) + ' ranking: ' + str(actor['ranking']))

        elif user_answer == 2:
            sorted_actors = sorted(all_actors, key=itemgetter('ranking'), )
            for actor in sorted_actors:
                print('name: ' + str(actor['name']) + ' Firstname: ' +
                      str(actor['firstname']) + ' ranking: ' + str(actor['ranking']))

    def report_all_players(self):
        players_table = db.table('players')
        all_players = players_table.all()
        tournament_table = db.table('tournaments')
        all_tournament = tournament_table.all()
        index = Views.indice_of_tournament()
        # use index to choose the right dico
        tournament = all_tournament[int(index)]
        players = []
        for player in tournament['players']:
            for play in all_players:
                if str(player) == str(play['name']):
                    players.append(play)

        user_answer = Views.sorted_report()
        if user_answer == 1:
            sorted_actors = sorted(players, key=itemgetter('name'), )
            for actor in sorted_actors:
                print('name: ' + str(actor['name']) + ' Firstname: ' +
                      str(actor['firstname']) + ' ranking: ' + str(actor['ranking']))

        elif user_answer == 2:
            sorted_actors = sorted(players, key=itemgetter('ranking'), )
            for actor in sorted_actors:
                print('name: ' + str(actor['name']) + ' Firstname: ' +
                      str(actor['firstname']) + ' ranking: ' + str(actor['ranking']))

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
