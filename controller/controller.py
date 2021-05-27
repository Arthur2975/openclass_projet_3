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
        # create or load tour
        list_of_players = []
        if self.tournament == "":
            user_answer = Views.print_create_or_load()
            if user_answer == 1:
                self.tournament = Views.create_new_tournament()
            elif user_answer == 2:
                self.tournament = Views.propose_to_load_tour()
            else:
                Views.print_create_or_load()
            # load players
            if len(self.tournament.players) != 0:
                players_names = self.tournament.players
                for player in players_names:
                    list_of_players.append(Player.load_player(player))
        # create players
        user_answer = Views.print_main_menu()
        if user_answer == 1:
            if Player.check_max_player(self.tournament.players):
                Views.players_full()
            else:
                player = Views.create_new_player()
                player.save()
                self.tournament.players.append(player.name)
            self.menu()

        # generate rounds
        elif user_answer == 2:
            self.generate_rounds()
            self.menu()
        # reports
        elif user_answer == 3:
            self.generate_reports(list_of_players)
            self.menu()
        # exit
        elif user_answer == 9:
            answer = Views.exit()
            if answer == 1:
                self.tournament.save()
                Views.tournament_saved()
                exit(0)
            if answer == 2:
                Views.goodbye()
                exit(0)
        else:
            self.menu()

    def generate_rounds(self, list_of_players):
        '''docstrings'''
        # create the round
        round = Views.create_round()
        # generate the round
        if round.name == 1:
            list_of_matchs = round.first_rnd(list_of_players)
        elif int(round.name) <= int(self.tournament.number_of_tours):
            list_of_matchs = round.round(list_of_players)
        elif int(round.name) > int(self.tournament.number_of_tours):
            Views.all_rounds_played()
            return

        list_of_players = []
        for match in list_of_matchs:
            for player in match:
                list_of_players.append(player)
                # append players to tournament
                self.tournament.players.append(player)
        # show generated matchs
        Views.show_match(list_of_matchs)
        # enter scores
        for match in list_of_matchs:
            score_1 = Views.propose_to_enter_scores(match[0].name)
            match[0].set_score(score_1)
            score_2 = Views.propose_to_enter_scores(match[1].name)
            match[1].set_score(score_2)
            # update matchs and scores in round
            round.match_list.append([(match[0].name, score_1), (match[1].name, score_2)])
        round.save()
        # add opponent
        for match in list_of_matchs:
            Player.add_opponents(match[0], match[1])
            Player.add_opponents(match[1], match[0])
        # update players
        player_table = db.table('players')
        player_table.truncate()
        for player in list_of_players:
            player.save()
        # update rounds in tournament
        self.tournament.rounds.append(round.name)
        # update players in tournament

        # final phrase and results
        if int(round.name) == int(self.tournament.number_of_tours):
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
            report.report_all_rounds()
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


# ya pas les jouerus dans le tournoi de la bd
# ya une couille dans les match list des round dans bd

# linker tournoi joueur
# rapports
# oral
