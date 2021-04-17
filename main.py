import json
from tinydb import TinyDB, Query
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
    match_first_round()
    match_second_round()


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

    # second match
    print('second match : ' +
          upper_group[1].name + ' against ' + lower_group[1].name)
    # enter scores:
    score_3 = input('Enter ' + upper_group[1].name + 's' + ' score')
    score_4 = input('Enter ' + lower_group[1].name + 's' + ' score')

    # third match
    print('third_match : ' +
          upper_group[2].name + ' against ' + lower_group[2].name)
    # Enter scores:
    score_5 = input('Enter ' + upper_group[2].name + 's' + ' score')
    score_6 = input('Enter ' + lower_group[2].name + 's' + ' score')

    # fourth match
    print('fourth_match : ' +
          upper_group[3].name + ' against ' + lower_group[3].name)
    # Enter scores:
    score_7 = input('Enter ' + upper_group[3].name + 's' + ' score')
    score_8 = input('Enter ' + lower_group[3].name + 's' + ' score')

    serialized_first_rnd_match = {'first_match': str(upper_group[0].name) + ' against ' + str(lower_group[0].name),
                                  'second_match': str(upper_group[1].name) + ' against ' + str(lower_group[1].name),
                                  'third_match': str(upper_group[2].name) + ' against ' + str(lower_group[2].name),
                                  'fourth_match': str(upper_group[3].name) + ' against ' + str(lower_group[3].name)}
    match_table = db.table('first_rnd_matchs')
    match_table.insert(serialized_first_rnd_match)

    serialized_first_rnd_scores = {upper_group[0].name: score_1, lower_group[0].name: score_2, upper_group[1].name: score_3,
                                   lower_group[1].name: score_4, upper_group[2].name: score_5,
                                   lower_group[2].name: score_6, upper_group[3].name: score_7,
                                   lower_group[3].name: score_8}
    scores_table = db.table('first_rnd_scores')
    scores_table.insert(serialized_first_rnd_scores)


def match_second_round():
    '''This function generates the second round's matchs. It generates pairs of players according to their first round's results, allow to enter scores
    and save it into the score file '''
    table_scores = db.table('first_rnd_scores')
    all_scores = table_scores.all()
    table_match = db.table('first_rnd_matchs')
    all_match = table_match.all()

    sorted_scores = sorted(
        all_scores[0].items(), key=lambda t: t[1], reverse=True)

    winners = []
    losers = []
    for tup in sorted_scores:
        if int(tup[1]) == 1:
            winners.append(tup[0])
        else:
            losers.append(tup[0])

    first_match = winners[0] + (' against ') + winners[1]
    second_match = winners[2] + (' against ') + winners[3]
    third_match = losers[0] + (' against ') + losers[1]
    fourth_match = losers[2] + (' against ') + losers[3]

    input('second tour, presse enter to generate a match')
    print(first_match)
    # enter score
    score_1 = input('enter score ' + winners[0])
    score_2 = input('enter score ' + winners[1])
    input('press enter to generate match')
    print(second_match)
    # enter score
    score_3 = input('enter score ' + winners[2])
    score_4 = input('enter score ' + winners[3])
    input('press enter to generate match')
    print(third_match)
    # enter score
    score_5 = input('enter score ' + losers[0])
    score_6 = input('enter score ' + losers[1])
    input('press enter to generate match')
    print(fourth_match)
    # enter score
    score_7 = input('enter score ' + losers[2])
    score_8 = input('enter score ' + losers[3])

    serialized_scores = {winners[0]: score_1, winners[1]: score_2, winners[2]: score_3, winners[3]: score_4,
                         losers[0]: score_5, losers[1]: score_6, losers[2]: score_7, losers[3]: score_8}
    scores_table = db.table('second_rnd_scores')
    scores_table.insert(serialized_scores)

    serialized_match = {'first_match': first_match, 'second_match': second_match,
                        'third_match': third_match,
                        'fourth_match': fourth_match}
    match_table = db.table('second_rnd_matchs')
    match_table.insert(serialized_match)

    '''changes dicos into tuples
    list_scores = all_scores[0].items()
    list_scores = list(list_scores)
    '''

    '''Morceau raté pour les nouvelles paires sans doublons
    for match in all_match[0]:
        for score in sorted_scores:
            print(score)
            if str(score) in match:
                print('match déjà joué')
                break
            else:
                first_match = (sorted_scores[0], sorted_scores[1])
                print('match = ' +
                      str(sorted_scores[0]) + str(sorted_scores[1]))
    '''
    # nimporte quoi: pas d'erreur mais fonctionne à chaque iteration avec les mêmes joueurs


def match_third_round():
    matchs_rnd1 = db.table('first_rnd_matchs')
    all_matchs_rnd1 = matchs_rnd1.all()
    matchs_rnd2 = db.table('second_rnd_matchs')
    all_matchs_rnd2 = matchs_rnd2.all()
    scores_rnd1 = db.table('first_rnd_scores')
    all_scores_rnd1 = scores_rnd1.all()
    scores_rnd2 = db.table('second_rnd_scores')
    all_scores_rnd2 = scores_rnd2.all()

    total_scores = {}
    for player in all_scores_rnd1[0]:
        for player_bis in all_scores_rnd2[0]:
            if str(player) == str(player_bis):
                total_scores.update({player:
                                     int(all_scores_rnd1[0][player]) + int(all_scores_rnd2[0][player_bis])})

    sorted_total_scores = sorted(
        total_scores.items(), key=lambda t: t[1], reverse=True)

    match_allready_played = []
    for value in all_matchs_rnd1[0].items():
        match_allready_played.append(value)
    for value in all_matchs_rnd2[0].items():
        match_allready_played.append(value)

    sorted_players = []
    for player in sorted_total_scores:
        sorted_players.append(player[0])

    match_list = []

    for player in sorted_players:
        if len(match_list) == len(sorted_total_scores):
            print('matchs allready generated')
            break
        elif player in match_list:
            pass
        elif len(match_list) == 0:
            match_list.append(player[0])
        else:
            player_index = sorted_players.index(player)
            next_player = player[int(player_index) + 1]
            for match in match_allready_played:
                next_player += 1
                if str(player) and str(next_player) in match:
                    pass


match_third_round()
