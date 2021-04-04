from tinydb import TinyDB, Query
import json
from classes import player as play
from classes import tournoi as tour


db = TinyDB('chess.json')


def new_tournament():
    ''' This function creates a new tournament and save it into a json file'''

    new_tournament = tour.Tournoi(
        input(' New tournament: \n Tournament_s name'), input(' place'), input('date'))
    tour.Tournoi.save(new_tournament)


def new_player():
    '''This function creates a new player and save it into a json file'''

    continue_while = True

    while continue_while == True:
        add_player = input('Do you want to add a new player? : Y/N')
        if add_player.lower() != 'y':
            break
        else:
            new_player = play.Player(input('name: '), input('firstname: '), input(
                'date_of_birth: '), input('gender: '), input('ranking: '))

        play.Player.save(new_player)


def main():
    '''this function is the main script that organizes the development of the program'''

    new_tournament()
    new_player()
    i = 0
    while i < 4:
        input('generating match pair, press enter')
        match_first_round()
        i += 1


def match_first_round():
    '''This function generates matchs between pairs of players, according to the 'swiss method' and allows to enter the scores of the matchs. The results
    are saved into a file'''

    table_player = db.table('players')
    all_players = table_player.all()

    list_player = []
    for player in all_players:
        list_player.append(play.Player(
            player['name'], player['firstname'], player['date_of_birth'], player['gender'], player['ranking']))

    sorted_list_player = sorted(list_player, key=lambda player: player.ranking)

    upper_group = []
    lower_group = []

    upper_group = sorted_list_player[:4]
    lower_group = sorted_list_player[4:8]

    # first match
    print('first_match : ' +
          upper_group[0].name + ' against ' + lower_group[0].name)
    # enter scores:
    score_1 = input('Enter ' + upper_group[0].name + 's' + ' score')
    score_2 = input('Enter ' + lower_group[0].name + 's' + ' score')
    first_match = (upper_group[0].name, score_1, lower_group[0].name, score_2)
    # second match
    print('second match : ' +
          upper_group[1].name + ' against ' + lower_group[1].name)
    # enter scores:
    score_3 = input('Enter ' + upper_group[1].name + 's' + ' score')
    score_4 = input('Enter ' + lower_group[1].name + 's' + ' score')
    second_match = (upper_group[1].name, score_3, lower_group[1].name, score_4)
    # third match
    print('third_match : ' +
          upper_group[2].name + ' against ' + lower_group[2].name)
    # Enter scores:
    score_5 = input('Enter ' + upper_group[2].name + 's' + ' score')
    score_6 = input('Enter ' + lower_group[2].name + 's' + ' score')
    third_match = (upper_group[2].name, score_5, lower_group[2].name, score_6)
    # fourth match
    print('fourth_match : ' +
          upper_group[3].name + ' against ' + lower_group[3].name)
    # Enter scores:
    score_7 = input('Enter ' + upper_group[3].name + 's' + ' score')
    score_8 = input('Enter ' + lower_group[3].name + 's' + ' score')
    fourth_match = (upper_group[3].name, score_7, lower_group[3].name, score_8)

    round_scores = [first_match, second_match, third_match, fourth_match]

    # with open('scores.json', 'w') as f_score:
    #     for item in round_scores:
    #         f_score.write(item)  # deconne veut pas enregistrer des tuples

    scores_table = db.table('scores')
    scores_table.insert(round_scores)  # serializer


def match_second_round():
    '''This function generates the second round's matchs. It generates pairs of players according to their first round's results, allow to enter scores
    and save it into the score file '''

    pass
    # trier les joueurs en fonction du nombre du points au premier tour
    # si même nombre de points, alors utiliser ranking
    # joueur 1 contre joueur 2, j3 contre j4 etc...
    # si les joueurs se sont déjà rencontrés alors joueur 1 contre j3

# trier la liste de joueur par ordre de points au premier tour.
# les gagnants ont 1 les perdants ont 0 donc si les 1 jouent entre eux et les zero entre eux il n'y a pas de doublons
# sorted_scores = sorted(liste of scores, key=lambda ...)
#import numpy as np
# a = np.array(tuples??)


# if __name__ == '__main__':
#     main()

match_first_round()
