import json
from tinydb import TinyDB, Query
from model import player as play
from model import tournoi as tour
import operator

db = TinyDB('chess.json')


class round:
    def __init__(self, name, date, hour):
        self.name = name
        self.date = date
        self.hour = hour
        self.match_list = []

    def add_match(self, match):
        self.match_list.append(match)

    def sort_list(list):
        return sorted(list, key=operator.attrgetter("score"), reverse=True)

    def match_first_round():
        '''This function generates matchs between pairs of players, according to the 'swiss method' and allows to enter the scores of the matchs. The results
        are saved into a file'''
        # get players db
        player_table = db.table('players')
        all_players = player_table.all()

        # deserialize players
        list_player = play.Player.deserialize_players(all_players)

        # seperate players in two groups
        sorted_list_player = sorted(
            list_player, key=lambda player: player.ranking)

        upper_group = []
        lower_group = []

        upper_group = sorted_list_player[:4]
        lower_group = sorted_list_player[4:8]

        # first match
        print('first_match : ' +
              upper_group[0].name + ' against ' + lower_group[0].name)
        # enter scores:
        score_1 = input('Enter ' + upper_group[0].name + 's' + ' score')
        play.Player.set_score(upper_group[0], score_1)
        play.Player.add_opponents(upper_group[0], lower_group[0])
        score_2 = input('Enter ' + lower_group[0].name + 's' + ' score')
        play.Player.set_score(lower_group[0], score_2)
        play.Player.add_opponents(lower_group[0], upper_group[0])

        # second match
        print('second match : ' +
              upper_group[1].name + ' against ' + lower_group[1].name)
        # enter scores:
        score_3 = input('Enter ' + upper_group[1].name + 's' + ' score')
        play.Player.set_score(upper_group[1], score_3)
        play.Player.add_opponents(upper_group[1], lower_group[1])
        score_4 = input('Enter ' + lower_group[1].name + 's' + ' score')
        play.Player.set_score(lower_group[1], score_4)
        play.Player.add_opponents(lower_group[1], upper_group[1])

        # third match
        print('third_match : ' +
              upper_group[2].name + ' against ' + lower_group[2].name)
        # Enter scores:
        score_5 = input('Enter ' + upper_group[2].name + 's' + ' score')
        play.Player.set_score(upper_group[2], score_5)
        play.Player.add_opponents(upper_group[2], lower_group[2])
        score_6 = input('Enter ' + lower_group[2].name + 's' + ' score')
        play.Player.set_score(lower_group[2], score_6)
        play.Player.add_opponents(lower_group[2], upper_group[2])

        # fourth match
        print('fourth_match : ' +
              upper_group[3].name + ' against ' + lower_group[3].name)
        # Enter scores:
        score_7 = input('Enter ' + upper_group[3].name + 's' + ' score')
        play.Player.set_score(upper_group[3], score_7)
        play.Player.add_opponents(upper_group[3], lower_group[3])
        score_8 = input('Enter ' + lower_group[3].name + 's' + ' score')
        play.Player.set_score(lower_group[3], score_8)
        play.Player.add_opponents(lower_group[3], upper_group[3])

        serialized_match = {'first_match': ([str(upper_group[0].name), score_1], [str(lower_group[0].name), score_2]),
                            'second_match': ([str(upper_group[1].name), score_3], [str(lower_group[1].name), score_4]),
                            'third_match': ([str(upper_group[2].name), score_5], [str(lower_group[2].name), score_6]),
                            'fourth_match': ([str(upper_group[3].name), score_7], [str(lower_group[3].name), score_8])}
        match_table = db.table('matchs')
        match_table.insert(serialized_match)

        # save players
        player_table = db.table('players')
        player_table.truncate()
        for player in list_player:
            play.Player.save(player)

    def match():
        # get db
        matchs_table = db.table('matchs')
        all_matchs = matchs_table.all()
        table_player = db.table('players')
        all_players = table_player.all()

        # deserialize players
        list_player = play.Player.deserialize_players(all_players)

        # sort player by scores
        sorted_players = round.sort_list(list_player)

        # pairing players
        players_with_match = []
        match_list = []

        for player in sorted_players:
            # verify the match weren't allready generated
            if len(players_with_match) == len(list_player):
                print('matchs generated')
                break
            else:
                # verify the player hasn't got a match allready
                if player in players_with_match:
                    continue
                else:
                    player_index = sorted_players.index(player)
                    for opponent in list_player:
                        if opponent in players_with_match:
                            continue
                        else:
                            if opponent == player:
                                continue
                            elif opponent.name in player.opponents_name:
                                continue
                            else:
                                match = (player, opponent)
                                break

                # actualize lists
                players_with_match.append(player)
                players_with_match.append(opponent)
                match_list.append(match)

                match_names = (player.name, opponent.name)
                print(match_names)
                score_1 = input('Enter {} _s score'.format(player.name))
                score_2 = input('Enter {} _s score'.format(opponent.name))
                play.Player.set_score(player, score_1)
                play.Player.set_score(opponent, score_2)
                play.Player.add_opponents(player, opponent)
                play.Player.add_opponents(opponent, player)

        # truncate et insert player_table
        table_player.truncate()
        for player in list_player:
            play.Player.save(player)

        # marche pas car score 3 à 8 n'existe plus, trouver autre technique avec les classe round pour récupérer les scores
        # faire une liste avec les scores et serializer
        '''
        # serialize and export matchs to db
        serialized_match = {'first match': ([match_list[0][0].name, score_1], [match_list[0][1].name, score_2]),
                            'second match': ([match_list[1][0].name, score_3], [match_list[1][1].name, score_4]),
                            'third match': ([match_list[2][0].name, score_5], [match_list[2][1].name, score_6]),
                            'fourth match': ([match_list[3][0].name, score_7], [match_list[3][1].name, score_8])}
        matchs_table.insert(serialized_match)
        '''
