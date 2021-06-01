from tinydb import TinyDB
from model.tournament import Tournament
from model.player import Player
from model.round import Round

db = TinyDB('chess.json')


class Views:
    '''docstring'''

    def print_create_or_load():
        user_answer = 0
        while user_answer not in (1, 2):
            print('Do you want to create or load a tournament?')
            print('Press 1: To create a new tournament')
            print('Press 2: To load an existing tournament')
            user_answer = input('Enter your choice: ')
            try:
                return int(user_answer)
            except:
                user_answer = 0

    def propose_to_load_tour():
        tournament = Tournament.load_tournament(input('tournament number: '))
        print('---------------------------------------')
        print('Tournament loaded')
        print('---------------------------------------')
        return tournament

    def print_main_menu():
        user_answer = 0
        while user_answer not in (1, 2, 3, 9):
            print('----')
            print('MENU')
            print('----')
            print('Press 1: To create a new player')
            print('Press 2: To create match')
            print('Press 3: To get reports')
            print('Press 9: To exit')
            user_answer = input('Enter your choice: ')
            try:
                return int(user_answer)
            except:
                user_answer = 0

    def create_new_tournament():
        tournament = Tournament(name=input('name: '), place=input('place: '), date=input('date: '))
        return tournament

    def create_new_player():
        player = Player(name=input('name: '), firstname=input('firstname: '), date_of_birth=input(
            'date_of_birth: '), gender=input('gender: '), ranking=input('ranking: '))
        return player

    def not_enough_players():
        print('------------------------------------')
        print('Not enough players to start a round')

    def players_full():
        print('------------------------------')
        print('Too many players for this tournament')

    def reports():
        print('--------------------------')
        print('Press 1 to view all actors')
        print('Press 2 to view all players')
        print('Press 3 to view all tournaments')
        print('Press 4 to view all rounds')
        print('Press 5 to view all match')
        user_answer = input('Enter your choice: ')

        return int(user_answer)

    def print_final_scores(list_of_players):
        print('Tournament is over!')
        input('press enter to visualize tournament results')
        print('scores:')
        for player in list_of_players:
            print(player.name + ': {}'.format(player.score))

    def show_match(list_of_match):
        for match in list_of_match:
            print('------------------------------------')
            print(match[0].name + ' against ' + match[1].name)

    def propose_to_enter_scores(player_name):
        user_answer = 3
        while user_answer not in (0, 0.5, 1):
            print('------------------------------------')
            print('please enter ' + str(player_name) + ' score: ')
            try:
                user_answer = float(input(
                    '0 for a loss, 0.5 for a spare, 1 for a win' + '\n' + 'Enter here: '))
                return user_answer
            except:
                user_answer = 3

    def propose_to_erase():
        print('Press 1: To erase the tournament infos')
        print('Press 2: To erase the players infos')
        user_answer = input('Enter your choice')
        return user_answer

    def exit():
        print('Do you want to save before you quit?: ')
        print('Press 1: Yes')
        print('Press 2: No')
        user_answer = input('Enter your choice: ')
        return int(user_answer)

    def tournament_saved():
        print('tournament saved, good bye')

    def create_round():
        while True:
            try:
                name = int(input('Enter the round number (1, 2, 3, 4): '))
                date = input('round_date: ')
                time = input('round_time')
                break

            except:
                print('Error in the entries')

        round = Round(name=name, date=date, time=time)
        return round

    def goodbye():
        print('Good bye')

    def all_rounds_played():
        print('__________________________')
        print('all rounds allready played')

    def sorted_report():
        user_answer = 0
        while user_answer not in (1, 2):
            print('Sorted by name, press 1: ')
            print('sorted by ranking, press 2: ')
            user_answer = input('enter your choice here: ')

            try:
                return int(user_answer)
            except:
                user_answer = 0

    def indice_of_tournament():
        while True:
            user_answer = input('what is the indice of the tournament for which you wanna see the players?')
            tournament_table = db.table('tournaments')
            all_tournaments = tournament_table.all()
            try:
                all_tournaments[int(user_answer)]
                return user_answer
            except:
                print('wrong indice, please try again')
                user_answer = False
