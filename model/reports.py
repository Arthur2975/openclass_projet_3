from tinydb import TinyDB
from operator import itemgetter
from views.views import Views

db = TinyDB('chess.json')


class Report:
    '''Class defining the different reports'''

    def __init__(self):
        pass

    def report_all_actors(self):
        '''reports all actors in the db'''
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
        '''reports all players in a tournament'''
        players_table = db.table('players')
        all_players = players_table.all()
        tournament_table = db.table('tournaments')
        all_tournament = tournament_table.all()
        user_answer = Views.which_name_tournament()
        players = []
        for tournament in all_tournament:
            if user_answer == tournament['name']:
                for player in tournament['players']:
                    for play in all_players:
                        if player == play['name']:
                            players.append(play)

        user_answer = Views.sorted_report()
        if user_answer == 1:
            sorted_players = sorted(players, key=itemgetter('name'))
            for player in sorted_players:
                print('name: ' + str(player['name']) + ' Firstname: ' +
                      str(player['firstname']) + ' ranking: ' + str(player['ranking']))

        elif user_answer == 2:
            sorted_players = sorted(players, key=itemgetter('ranking'))
            for player in sorted_players:
                print('name: ' + str(player['name']) + ' Firstname: ' +
                      str(player['firstname']) + ' ranking: ' + str(player['ranking']))

    def report_all_tournaments(self):
        '''reports all tournament saved in the db'''
        tournaments_table = db.table('tournaments')
        all_tournaments = tournaments_table.all()
        for tournament in all_tournaments:
            print('------------')
            print('name: ' + str(tournament['name']) + ', place: ' +
                  str(tournament['place']) + ', date: ' + str(tournament['date']))

    def report_rounds_tournament(self):
        '''reports all rounds in a certain tournamnent'''
        rounds_table = db.table('rounds')
        all_rounds = rounds_table.all()
        user_answer = Views.which_name_tournament()
        for round in all_rounds:
            if round['tournament_name'] == user_answer:
                print('-------------')
                print('name: ' + str(round['name']), 'date: ' + str(round['date']), 'time: ' + str(round['time']))

    def report_matchs_tournament(self):
        '''reports all matchs in a certain tournament'''
        rounds_table = db.table('rounds')
        all_rounds = rounds_table.all()
        user_answer = Views.which_name_tournament()
        for round in all_rounds:
            print('-----------------')
            print('Round: ')
            print(round['name'])
            if round['tournament_name'] == user_answer:
                match_list = round['match_list']
                for match in match_list:
                    print(match[0][0] + ' against ' + match[1][0])
