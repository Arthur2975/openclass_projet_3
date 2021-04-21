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

    serialized_match = {'first_match': ([str(upper_group[0].name), score_1], [str(lower_group[0].name), score_2]),
                        'second_match': ([str(upper_group[1].name), score_3], [str(lower_group[1].name), score_4]),
                        'third_match': ([str(upper_group[2].name), score_5], [str(lower_group[2].name), score_6]),
                        'fourth_match': ([str(upper_group[3].name), score_7], [str(lower_group[3].name), score_8])}
    match_table = db.table('matchs')
    match_table.insert(serialized_match)


def match():

    # recreate instances of players
    table_player = db.table('players')
    all_players = table_player.all()

    list_player = []
    for player in all_players:
        list_player.append(play.Player(
            player['name'], player['firstname'], player['date_of_birth'], player['gender'], player['ranking']))

    # get db
    matchs_table = db.table('matchs')
    all_matchs = matchs_table.all()

    # add scores
    # initialize list of cumulated scores
    total_scores = {}
    for player in list_player:
        total_scores[player.name] = 0

    scores = []
    for round in all_matchs:
        for key, value in all_matchs[0].items():
            tup_score = tuple(value)
            scores.append(tup_score)

    for tuple_ in scores:
        for liste in tuple_:
            for score in total_scores:
                if str(liste[0]) == str(score):
                    total_scores[score] += int(liste[1])

    # sort players by score
    sorted_total_scores = sorted(
        total_scores.items(), key=lambda t: t[1], reverse=True)

    # liste of match that have already been played
    match_already_played = []
    for element in all_matchs:
        for key, value in element.items():
            match_already_played.append(value)

    # liste of players by score
    sorted_players = []
    for player in sorted_total_scores:
        sorted_players.append(player[0])

    match_list = []
    players_with_match = []

    # get all players
    players = db.table('players')
    all_players = players.all()

    # check if all match have been created for the round
    if len(players_with_match) == len(all_players):
        print('All matchs generated')

    else:
        for player in sorted_players:
            player_index = sorted_players.index(player)

            # pair with the next player

            if len(players_with_match) == len(all_players):
                print('All matchs generated')
                break
            if player_index != len(all_players)-1:
                while player in players_with_match:
                    player_index += 1
                    player = sorted_players[player_index]

            if player_index != len(all_players)-1:
                next_player = sorted_players[player_index + 1]
                index = 1
                # check the next player doesnt have a match already
                while next_player in players_with_match:
                    index += 1
                    next_player = sorted_players[player_index + index]
                    for match in match_already_played:
                        # check the player and the next player didnt compete already in the other rounds
                        while str(player) and str(next_player) in match:
                            index += 1
                            next_player = sorted_players[player_index + index]

                # actualize lists of match and players still free
                actual_match = (player, next_player)
                match_list.append(actual_match)
                players_with_match.append(player)
                players_with_match.append(next_player)
                print(actual_match)

    # add scores
    score_1 = input('enter' + match_list[0][0] + 'score')
    score_2 = input('enter' + match_list[0][1] + 'score')
    score_3 = input('enter' + match_list[1][0] + 'score')
    score_4 = input('enter' + match_list[1][1] + 'score')
    score_5 = input('enter' + match_list[2][0] + 'score')
    score_6 = input('enter' + match_list[2][1] + 'score')
    score_7 = input('enter' + match_list[3][0] + 'score')
    score_8 = input('enter' + match_list[3][1] + 'score')

    # serialize and export matchs to db
    serialized_match = {'first match': ([match_list[0][0], score_1], [match_list[0][1], score_2]),
                        'second match': ([match_list[1][0], score_3], [match_list[1][1], score_4]),
                        'third match': ([match_list[2][0], score_5], [match_list[2][1], score_6]),
                        'fourth match': ([match_list[3][0], score_7], [match_list[3][1], score_8])}
    matchs_table.insert(serialized_match)


def main():
    '''this function is the main script that organizes the development of the program'''

    new_tournament()
    new_player()
    match_first_round()
    match_second_round()
    match_third_round()


match()
