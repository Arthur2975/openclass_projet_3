from tinydb import TinyDB, Query
from views.views import Views
from model.player import Player
from model.reports import Report

db = TinyDB('chess.json')


class Controller:
    '''class controller'''

    def __init__(self, tournament):
        self.tournament = tournament

    def menu(self):
        '''Main menu of the program, makes the link between
        the views and the models to allow the user access
        every fonctionality of the application'''
        # create or load tour
        if self.tournament == "":
            user_answer = Views.print_create_or_load()
            # if user wants to create tour
            if user_answer == 1:
                self.tournament = Views.create_new_tournament()
            # if user wants to load a tour
            elif user_answer == 2:
                self.tournament = Views.propose_to_load_tour()
            # other answer
            else:
                Views.print_create_or_load()
            # load players if players that allready are in the loaded tour
            if len(self.tournament.players) != 0:
                for player in self.tournament.players:
                    self.tournament.players_i.append(Player.load_player(player))

        # create players
        user_answer = Views.print_main_menu()
        if user_answer == 1:
            # check if there is too many players
            if Player.check_max_player(self.tournament.players):
                Views.players_full()
            # create the player
            else:
                player = Views.create_new_player()
                # add to the list of players
                self.tournament.players_i.append(player)
                # add to the tour instance
                self.tournament.players.append(player.name)
            self.menu()

        # generate rounds
        elif user_answer == 2:
            # check if there is enough players
            if len(self.tournament.players) == int(self.tournament.number_of_players):
                # generate the round with the list of players
                self.generate_rounds(self.tournament.players_i)
                self.menu()
            # if not enough players return an alert
            else:
                Views.not_enough_players()
                self.menu()

        # go to the reports menu
        elif user_answer == 3:
            self.generate_reports()
            self.menu()
        # exit
        elif user_answer == 9:
            answer = Views.exit()
            # if wants to save
            if answer == 1:
                # erase the players in the db
                # save the players in list of players
                players_table = db.table('players')
                play = Query()
                for player in self.tournament.players_i:
                    players_table.remove(play.name == player.name)
                    player.save()
                # erase list of player instances to save
                self.tournament.players_i = []
                # erase the tournaments in the db
                tournament_table = db.table('tournaments')
                tour = Query()
                tournament_table.remove(tour.name == self.tournament.name)
                # save the tour
                self.tournament.save()
                Views.tournament_saved()
                exit(0)
            if answer == 2:
                Views.goodbye()
                exit(0)
        else:
            self.menu()

    def generate_rounds(self, list_of_players):
        '''Makes the link between the round model and the views
        in order to generate the rounds and pair the players'''
        # create the round
        round = Views.create_round()
        round.tournament_name = self.tournament.name
        # initialize match list because python keep in memory the last match list in the instance round
        round.match_list = []
        # generate the round and return the list of matchs
        # if it is the first round, lauch first round algorithm
        if int(round.name) == 1:
            list_of_matchs = round.first_rnd(list_of_players)
        # if it is a round other than the first one
        elif int(round.name) > 1 and int(round.name) <= int(self.tournament.number_of_tours):
            list_of_matchs = round.round(list_of_players)
        # if the number of rounds is exceeded
        else:
            Views.all_rounds_played()
            return
        # show generated matchs
        Views.show_match(list_of_matchs)
        # enter scores
        for match in list_of_matchs:
            # enter player's score for each match
            score_1 = Views.propose_to_enter_scores(match[0].name)
            # set the score in the player instance
            match[0].set_score(score_1)
            # same procedure for the second player of the match
            score_2 = Views.propose_to_enter_scores(match[1].name)
            match[1].set_score(score_2)
            # update in round, each match and scores
            round.match_list.append([(match[0].name, score_1), (match[1].name, score_2)])
        # save the round in the db
        round.save()
        # add opponent in each player instance
        for match in list_of_matchs:
            match[0].add_opponents(match[1])
            match[1].add_opponents(match[0])
        # update players in list of instances in tournament
        list_play_instances = []
        for match in list_of_matchs:
            for player in match:
                list_play_instances.append(player)
        self.tournament.players_i = list_play_instances
        # update rounds list in the tournament instance
        self.tournament.rounds.append(round.name)
        # final phrase and results if the round is the last one
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
            report.report_rounds_tournament()
        elif user_answer == 5:
            report.report_matchs_tournament()


# le pb c'est que opponent est toujours dans opponent.name, dans generate round --> first round ca doit ajouter tous les opponents à chaque instance
# line 130 dans controler ca rajoute a chaque player toute la liste d'opponents
# oral

# bloquer la user answer du numeor de tournament a loader
