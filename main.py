from tinydb import TinyDB
from classes import player 
from classes import tournoi


def new_player():
    #new players
    new_player = player.Player(input(' name'), input(' firstname'), input(' date_of_birth'), input(' gender'), input(' ranking'))
    player.Player.save(new_player)

def new_tournament():
    #new tournament
    new_tournament = tournoi.Tournoi(input(' name'), input(' place'), input('date'))
    tournoi.Tournoi.save(new_tournament)


new_tournament()

