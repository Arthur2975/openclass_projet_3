from tinydb import TinyDB
from model import tournoi as tour
from view import views
from model import round as rnd
from model import player as play

db = TinyDB('chess.json')


class Controller:
    '''class controller'''

    def __init__(self):
        pass

    def main_menu(self):
        '''docstring'''
        user_answer = views.Views.print_main_menu()
        if user_answer == 1:
            tour.Tournoi.new_tournament()
            self.main_menu()
        elif user_answer == 2:
            tour.Tournoi.new_player()
            self.main_menu()
        elif user_answer == 3:
            self.generate_rounds()
            self.main_menu()
        elif user_answer == 4:
            self.save()
            self.main_menu()
        elif user_answer == 5:
            self.load()
            self.main_menu()
        elif user_answer == 6:
            self.erase_db()
            self.main_menu()
        elif user_answer == 7:
            pass
            self.main_menu()
        elif user_answer == 8:
            self.generate_reports()
            self.main_menu()
        else:
            self.main_menu()

    def generate_rounds(self):
        '''docstrings'''
        # generate rounds
        tournament_table = db.table('tournaments')
        db_tournament = tournament_table.all()
        tournament = tour.Tournoi(
            name=db_tournament[0]['name'], place=db_tournament[0]['place'], date=db_tournament[0]['date'])
        continue_while = 0
        round_index = 1
        while continue_while < int(tournament.number_of_tours):
            # generate the first rnd
            list_of_matchs = rnd.Round.all_rounds(round_index)
            list_of_players = []
            for match in list_of_matchs:
                for player in match:
                    list_of_players.append(player)
            # show generated matchs
            views.Views.show_match(list_of_matchs)
            # enter scores
            for match in list_of_matchs:
                for player in match:
                    score = views.Views.propose_to_enter_scores(player.name)
                    play.Player.set_score(
                        player, score)
            # add opponent
            for match in list_of_matchs:
                play.Player.add_opponents(match[0], match[1])
                play.Player.add_opponents(match[1], match[0])
            # update players
            player_table = db.table('players')
            player_table.truncate()
            for player in list_of_players:
                play.Player.save(player)
            round_index += 1
            continue_while += 1

        # final phrase and results
        views.Views.print_final_scores(list_of_players)

    def save(self):
        pass

    def load(self):
        pass

    def generate_reports(self):
        '''docstring'''
        user_answer = views.Views.reports()
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
        user_answer = views.Views.propose_to_erase()
        if user_answer == 1:
            tournament_table = db.table('tournaments')
            tournament_table.truncate()
        elif user_answer == 2:
            players_table = db.table('players')
            players_table.truncate()


# creer classe rapport dans les model qui fait tout ca
