from tinydb import TinyDB
import operator

db = TinyDB('chess.json')


class Round:
    '''This class defines a round and its attributes'''

    def __init__(self, name, date, time, tournament_name='tournament', match_list=[]):
        self.name = name
        self.date = date
        self.time = time
        self.tournament_name = tournament_name
        self.match_list = match_list

    def add_match(self, match):
        '''adds match to a match list'''
        self.match_list.append(match)

    def sort_list(list):
        '''sorts a list of players by their scores'''
        return sorted(list, key=operator.attrgetter("score"), reverse=True)

    def first_rnd(self, list_of_players):
        '''returns a list of match paired by ranking,
        according to the swiss algorithm'''

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

    def round(self, list_player):
        '''Returns a list of match paired by
        their previous scores in the tournament'''

        # sort player by scores
        sorted_players = Round.sort_list(list_player)

        # pairing players
        players_with_match = []
        match_list = []

        for player in sorted_players:
            print('player: ' + player.name)
            # verify the match weren't allready generated
            if len(players_with_match) == len(list_player):
                print('--------------------')
                break
            else:
                # verify the player has no match allready
                if player in players_with_match:
                    continue
                else:
                    for opponent in list_player:
                        print('opponent: ' + opponent.name)
                        if opponent in players_with_match:
                            continue
                        else:
                            print(opponent == player)
                            print(opponent.name in player.opponents_name)
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

    def save(self):
        '''save a round in the db'''
        serialized_round = {'name': self.name, 'date': self.date,
                            'time': self.time, 'match_list': self.match_list, 'tournament_name': self.tournament_name}
        round_table = db.table('rounds')
        round_table.insert(serialized_round)
