from tinydb import TinyDB, Query

class Match:
    def __init__(self, index, player_1, player_2, score_1, score_2):
        self.index = index
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def save match():
        serialized_match = {'player_1': player_1, 'player_2': player_2, 'score_1': score_1, 'score_2': score_2}
        db = TinyDB('match.json')
        db.insert(Match(serialized_match))


    def get_score(self, ):

    def generate_pair():


    #input --> import 2 joueurs du Json
    # load jsais pas quoi
    #faire un algorithme qui choisi

    #output --> un tuple contenant 2 listes avec joueur et score, ex: ([player_1, score_1], [player_2, score_2])


#génération des paires
#8 joueurs: divisés en deux groupes (ranking). 
# Joueur 1 avec 5
# joueur 2 avec 6
# joueur 3 avec 7 
# joueur 4 avec 8

'''

lower_group = []
upper_group = []
if self.ranking > 4:
    lower_group.append(player)
elif self.ranking < 4:
    upper_group.append(player)
else:
    return 'wrong ranking'

for player in upper_group:
    player_1 = player

for player in lower_group:
    player_2 = player

'''
