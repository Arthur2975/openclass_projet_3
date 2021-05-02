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
    continue_while = 0
    while continue_while <= 4:
        rnd.round.match()
        continue_while += 1


if __name__ == '__main__':
    main()
