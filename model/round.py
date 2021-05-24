from tinydb import TinyDB
from model import player as play
import operator

db = TinyDB('chess.json')


class Round:
    def __init__(self, name, date, time, match_list=[]):
        self.name = name
        self.date = date
        self.time = time
        self.match_list = match_list

    def add_match(self, match):
        self.match_list.append(match)

    def sort_list(list):
        return sorted(list, key=operator.attrgetter("score"), reverse=True)

    def first_rnd():
        '''docstring'''
        player_table = db.table('players')
        all_players = player_table.all()

        list_of_players = play.Player.deserialize_players(all_players)
        sorted_players = sorted(
            list_of_players, key=lambda player: player.ranking)

        higher_players = []
        lower_players = []

        higher_players.append(sorted_players[:4])
        lower_players.append(sorted_players[4:8])

        matchs_first_round = [(higher_players[0][0], lower_players[0][0]),
                              (higher_players[0][1], lower_players[0][1]),
                              (higher_players[0][2], lower_players[0][2]),
                              (higher_players[0][3], lower_players[0][3])]

        return matchs_first_round

    def round():
        # get db
        table_player = db.table('players')
        all_players = table_player.all()

        # deserialize players
        list_player = play.Player.deserialize_players(all_players)

        # sort player by scores
        sorted_players = Round.sort_list(list_player)

        # pairing players
        players_with_match = []
        match_list = []

        for player in sorted_players:
            # verify the match weren't allready generated
            if len(players_with_match) == len(list_player):
                print('matchs over')
                print('--------------------')
                print('Next round')
                break
            else:
                # verify the player hasn't got a match allready
                if player in players_with_match:
                    continue
                else:
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

        return match_list

    def all_rounds(round_index):
        if round_index == 1:
            return Round.first_rnd()
        else:
            return Round.round()

    def save(self):
        serialized_match = {'name': self.name, 'date': self.date,
                            'time': self.time, 'match_list': self.match_list}
        round_table = db.table('rounds')
        round_table.insert(serialized_match)

    def load(self):
        pass
