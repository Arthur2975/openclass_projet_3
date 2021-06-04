from tinydb import TinyDB
from model.tournament import Tournament
from model.player import Player
from model.round import Round

db = TinyDB('chess.json')


class Views:
    '''defines the views and methods'''

    def print_create_or_load():
        '''propose to create or load an existing tournament'''
        user_answer = 0
        while user_answer not in (1, 2):
            print('Do you want to create or load a tournament?')
            print('Press 1: To create a new tournament')
            print('Press 2: To load an existing tournament')
            user_answer = input('Enter your choice: ')
            try:
                return int(user_answer)
            except ValueError:
                user_answer = 0

    def propose_to_load_tour():
        '''propose the user to enter the name of the tournament he wants to load
        and loads the proper tournament from the db'''
        while True:
            tournament_table = db.table('tournaments')
            all_tournaments = tournament_table.all()
            tour_name = input('Tournament name: ')
            for tournament in all_tournaments:
                if tournament['name'] == tour_name:
                    user_answer = Tournament.load_tournament(tournament)
                    print('---------------------------------------')
                    print('Tournament loaded')
                    print('---------------------------------------')
                    return user_answer
                else:
                    print('-------------')
                    print('wrong entries')

    def print_main_menu():
        '''main menu of the program'''
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
            except ValueError:
                user_answer = 0

    def create_new_tournament():
        '''allows the use to create a new tournament'''
        tournament = Tournament(name=input('name: '), place=input('place: '), date=input('date: '))
        return tournament

    def create_new_player():
        '''allows the user to create a new player'''
        player = Player(name=input('name: '), firstname=input('firstname: '), date_of_birth=input(
            'date_of_birth: '), gender=input('gender: '), ranking=input('ranking: '), opponents_name=[])
        return player

    def not_enough_players():
        '''print an alert when the user wants to make a match
        without the proper amount of players'''
        print('------------------------------------')
        print('Not enough players to start a round')

    def players_full():
        '''prints an alert when the user wants to add
        too many players'''
        print('------------------------------')
        print('Too many players for this tournament')

    def reports():
        '''reports menu'''
        print('--------------------------')
        print('Press 1 to view all actors')
        print('Press 2 to view all players')
        print('Press 3 to view all tournaments')
        print('Press 4 to view all rounds of a tournament')
        print('Press 5 to view all matchs of a tournament')
        user_answer = input('Enter your choice: ')

        return int(user_answer)

    def print_final_scores(list_of_players):
        '''print the final score of each player'''
        print('Tournament is over!')
        input('press enter to visualize tournament results')
        print('scores:')
        for player in list_of_players:
            print(player.name + ': {}'.format(player.score))

    def show_match(list_of_match):
        '''print the matchs from a list of matchs'''
        for match in list_of_match:
            print('------------------------------------')
            print(match[0].name + ' against ' + match[1].name)

    def propose_to_enter_scores(player_name):
        '''let the user enter a match's scores'''
        user_answer = 3
        while user_answer not in (0, 0.5, 1):
            print('------------------------------------')
            print('please enter ' + str(player_name) + ' score: ')
            try:
                user_answer = float(input(
                    '0 for a loss, 0.5 for a spare, 1 for a win' + '\n' + 'Enter here: '))
                return user_answer
            except ValueError:
                user_answer = 3

    def exit():
        '''exit menu, propose to save before'''
        print('Do you want to save before you quit?: ')
        print('Press 1: Yes')
        print('Press 2: No')
        user_answer = input('Enter your choice: ')
        return int(user_answer)

    def tournament_saved():
        '''print that the tournament was saved'''
        print('tournament saved, good bye')

    def create_round():
        '''let the user create an instance of round'''
        while True:
            try:
                name = int(input('Enter the round number (1, 2, 3, 4): '))
                date = input('round_date: ')
                time = input('round_time')
                break

            except ValueError:
                print('Error in the entries')

        round = Round(name=name, date=date, time=time)
        return round

    def goodbye():
        '''print goodby when exit'''
        print('Good bye')

    def all_rounds_played():
        '''print an alert when the match are all paired'''
        print('__________________________')
        print('all rounds allready played')

    def sorted_report():
        '''propose to sort by name or by score'''
        user_answer = 0
        while user_answer not in (1, 2):
            print('Sorted by name, press 1: ')
            print('sorted by ranking, press 2: ')
            user_answer = input('enter your choice here: ')

            try:
                return int(user_answer)
            except ValueError:
                user_answer = 0

    def which_name_tournament():
        '''ask the user the name of the tournament he wants to load or analyse'''
        while True:
            print('Whats the name of the tournament you want to see the infos?: ')
            user_answer = input('Enter your choice here: ')
            tournament_table = db.table('tournaments')
            all_tournaments = tournament_table.all()
            for tournament in all_tournaments:
                if tournament['name'] == str(user_answer):
                    return user_answer
                else:
                    print('-------------')
                    print('wrong entries')
