import json
from tinydb import TinyDB, Query
from model import player as play
from model import tournoi as tour
from model import round as rnd
import operator

db = TinyDB('chess.json')


def main():
    '''this function is the main script that organizes the development of the program'''

    tour.Tournoi.new_tournament()
    tour.Tournoi.new_player()
    rnd.round.match_first_round()
    tournament_table = db.table('tournaments')
    db_tournament = tournament_table.all()
    tournament = tour.Tournoi(
        name=db_tournament[0]['name'], place=db_tournament[0]['place'], date=db_tournament[0]['date'])
    continue_while = 2
    while continue_while < int(tournament.number_of_tours):
        rnd.round.match()
        continue_while += 1
    print('Tournament over!')
    input('press enter to visualize tournament results')
    print('scores: blabla')


if __name__ == '__main__':
    main()

# role du main juste appeler le controleur
# mettre tous les trucs du main dans ctrlr
# mvc + flake 8
