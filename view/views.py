from tinydb import TinyDB

db = TinyDB('chess.json')


class Views:
    '''docstring'''
    def print_main_menu():
        user_answer = 0
        while user_answer not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            print('Chess tournament')
            print('----------------')
            print('Press 1: To create the tournament')
            print('Press 2: To create a new player')
            print('Press 3: To create match')
            print('Press 4: Save')
            print('Press 5: load')
            print('Press 6: Erase tournaments or players')
            print('Press 7: ')
            print('Press 8: To get reports')
            print('Press 9: To exit')
            user_answer = input('Enter your choice: ')

            return int(user_answer)

    def reports():
        print('Press 1 to view all actors')
        print('Press 2 to view all players')
        print('Press 4 to view all tournaments')
        print('Press 5 to view all tournee')
        print('Press 6 to view all match')
        user_answer = input('Enter your choice: ')

        return user_answer

    def print_final_scores(list_of_players):
        print('Tournament is over!')
        input('press enter to visualize tournament results')
        print('scores:')
        for player in list_of_players:
            print(player.name + ': {}'.format(player.score))

    def show_match(list_of_match):
        for match in list_of_match:
            print(match[0].name + ' against ' + match[1].name)

    def propose_to_enter_scores(player_name):
        user_answer = 3
        while user_answer not in [0, 0.5, 1]:
            print('please enter ' + str(player_name) + ' score: ')
            user_answer = input(
                '0 for a loss, 0.5 for a spare, 1 for a win' + '\n' + 'Enter here: ')
        return float(user_answer)

    def propose_to_erase():
        print('Press 1: To erase the tournament infos')
        print('Press 2: To erase the players infos')
        user_answer = input('Enter your choice')
