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
        self.first_match = []

    def add_match(self):
        pass

    def match():
        # get db
        matchs_table = db.table('matchs')
        all_matchs = matchs_table.all()
        table_player = db.table('players')
        all_players = table_player.all()

        # recreate instances of players
        list_player = []
        for player in all_players:
            list_player.append(play.Player(
                player['name'], player['firstname'], player['date_of_birth'], player['gender'], player['ranking'], player['score'], player['opponents']))

        # sort player by scores
        sorted_players = sorted(
            list_player, key=operator.attrgetter("score"), reverse=True)

        # apparing with objects
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
                            elif opponent.name in player.opponents:
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
        '''
        # serialize and export matchs to db
        serialized_match = {'first match': ([match_list[0][0].name, score_1], [match_list[0][1].name, score_2]),
                            'second match': ([match_list[1][0].name, score_3], [match_list[1][1].name, score_4]),
                            'third match': ([match_list[2][0].name, score_5], [match_list[2][1].name, score_6]),
                            'fourth match': ([match_list[3][0].name, score_7], [match_list[3][1].name, score_8])}
        matchs_table.insert(serialized_match)
        '''
