from tinydb import TinyDB
from model.tournament import Tournament
from views.views import Views
from model.round import Round
from model.player import Player
from model.reports import Report

db = TinyDB('chess.json')


class Controller:
    '''class controller'''

    def __init__(self, tournament):
        self.tournament = tournament

    def menu(self):
        '''docstring'''
        if self.tournament == "":
            user_answer = Views.print_create_or_load()
            if user_answer == 1:
                self.tournament = Views.create_new_tournament()
            elif user_answer == 2:
                self.tournament = Tournament.load_tournament(input('tournament number: '))
                print('---------------------------------------')
                print('Tournament loaded: ' + self.tournament.name)
                print('---------------------------------------')
            else:
                Views.print_create_or_load()

        user_answer = Views.print_main_menu()
        if user_answer == 1:
            if Player.check_max_player():
                print('------------------------------')
                print('Nombre de joueurs max atteint')
            else:
                player = Views.create_new_player()
                player.save()
            self.menu()
        elif user_answer == 2:
            self.generate_rounds()
            self.menu()
        elif user_answer == 3:
            self.erase_db()
            self.menu()
        elif user_answer == 4:
            self.generate_reports()
            self.menu()
        elif user_answer == 9:
            answer = Views.exit()
            if answer == 1:
                self.tournament.save()
                print('tournament saved, good bye')
                exit(0)
            if answer == 2:
                print('good bye!')
                exit(0)
        else:
            self.main_menu()

    def generate_rounds(self):
        '''docstrings'''
        # generate rounds
        round = Round(name=input('round_name: '), date=input('round_date: '), time=input('round_time'))
        tournament_table = db.table('tournaments')
        db_tournament = tournament_table.all()
        tournament = Tournament(
            name=db_tournament[0]['name'], place=db_tournament[0]['place'], date=db_tournament[0]['date'])
        round_index = 1
        if len(self.tournament.rounds) < int(tournament.number_of_tours):
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
            # update round
            for match in list_of_matchs:
                for player in match:
                    round.match_list.append(player.name)
            round.save()
            # update rounds in tournament
            tournament.rounds.append(round.name)
            tournament.save()

        else:
            print('all rounds allready played')

        # final phrase and results
        if int(round.name) == int(tournament.number_of_tours):
            Views.print_final_scores(list_of_players)

    def generate_reports(self):
        '''docstring'''
        report = Report()
        user_answer = Views.reports()
        if user_answer == 1:
            report.report_all_actors()
        elif user_answer == 2:
            report.report_all_players()
        elif user_answer == 3:
            report.report_all_tournaments()
        elif user_answer == 4:
            report.report_all_tournee()
        elif user_answer == 5:
            report.report_all_match()

    def erase_db(self):
        user_answer = Views.propose_to_erase()
        if user_answer == 1:
            tournament_table = db.table('tournaments')
            tournament_table.truncate()
        elif user_answer == 2:
            players_table = db.table('players')
            players_table.truncate()

    def main(self):
        tournoi = self.create_or_load()
        self.menu()
