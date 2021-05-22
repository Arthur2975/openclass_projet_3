from tinydb import TinyDB
from model.tournament import Tournament
from views.views import Views
from model.round import Round
from model.player import Player

db = TinyDB('chess.json')


class Controller:
    '''class controller'''

    def __init__(self):
        pass

    def create_or_load(self):
        user_answer = Views.print_create_or_load()
        if user_answer == 1:
            tournament = Views.create_new_tournament()
        elif user_answer == 2:
            tournament = Tournament.load_tournament(input('tournament number: '))
        else:
            Views.print_create_or_load()

    def main_menu(self):
        '''docstring'''
        user_answer = Views.print_main_menu()
        if user_answer == 1:
            Tournament.new_tournament()
            self.main_menu()
        elif user_answer == 2:
            Tournament.new_player()
            self.main_menu()
        elif user_answer == 3:
            self.generate_rounds()
            self.main_menu()
        elif user_answer == 4:
            self.erase_db()
            self.main_menu()
        elif user_answer == 5:
            self.generate_reports()
            self.main_menu()
        elif user_answer == 9:
            answer = Views.exit()
            if answer == 1:
                Tournament.save()
                Player.save()
                self.main_menu()
            if answer == 2:
                print('good bye!')
                exit(0)
        else:
            self.main_menu()

    def generate_rounds(self):
        '''docstrings'''
        # generate rounds
        tournament_table = db.table('tournaments')
        db_tournament = tournament_table.all()
        tournament = Tournoi(
            name=db_tournament[0]['name'], place=db_tournament[0]['place'], date=db_tournament[0]['date'])
        continue_while = 0
        round_index = 1
        while continue_while < int(tournament.number_of_tours):
            # generate the first rnd
            list_of_matchs = Round.all_rounds(round_index)
            list_of_players = []
            for match in list_of_matchs:
                for player in match:
                    list_of_players.append(player)
            # show generated matchs
            Views.show_match(list_of_matchs)
            # enter scores
            for match in list_of_matchs:
                for player in match:
                    score = Views.propose_to_enter_scores(player.name)
                    Player.set_score(
                        player, score)
            # add opponent
            for match in list_of_matchs:
                Player.add_opponents(match[0], match[1])
                Player.add_opponents(match[1], match[0])
            # update players
            player_table = db.table('players')
            player_table.truncate()
            for player in list_of_players:
                Player.save(player)
            round_index += 1
            continue_while += 1

        # final phrase and results
        Views.print_final_scores(list_of_players)

    def generate_reports(self):
        '''docstring'''
        user_answer = Views.reports()
        if user_answer == 1:
            self.report_all_actors()
        elif user_answer == 2:
            self.report_all_players()
        elif user_answer == 3:
            self.report_all_tournaments()
        elif user_answer == 4:
            self.report_all_tournee()
        elif user_answer == 5:
            self.report_all_match()

    def report_all_actors(self):
        actors_table = db.table('players')
        all_actors = actors_table.all()
        print(all_actors)

    def report_all_players(self):
        players_table = db.table('players')
        all_players = players_table.all()
        print(all_players)

    def report_all_tournaments(self):
        tournaments_table = db.table('tournaments')
        all_tournaments = tournaments_table.all()
        print(all_tournaments)

    def report_all_tournee(self):
        pass

    def report_all_match(self):
        pass

    def erase_db(self):
        user_answer = Views.propose_to_erase()
        if user_answer == 1:
            tournament_table = db.table('tournaments')
            tournament_table.truncate()
        elif user_answer == 2:
            players_table = db.table('players')
            players_table.truncate()


# creer classe rapport dans les model qui fait tout ca
