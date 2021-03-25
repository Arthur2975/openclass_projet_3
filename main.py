from tinydb import TinyDB
import json
from classes import player 
from classes import tournoi


def new_tournament():
    #new tournament
    new_tournament = tournoi.Tournoi(input(' name'), input(' place'), input('date'))
    tournoi.Tournoi.save(new_tournament)


def new_player():
    #new players
    continue_while = True
    
    while continue_while == True:
        add_player = input('Do you want to add a new player? : Y/N')
        if add_player.lower() != 'y':
            break
        else:
            new_player = player.Player(input('name: '), input('firstname: '), input('date_of_birth: '), input('gender: '), input('ranking: '))

        player.Player.save(new_player)
    

def generate_matchs():

    with open('chess.json') as my_json_file:
        data = json.load(my_json_file)
    

    lower_group = []
    upper_group = []

    if len(data['players']) != 8:
        print('nombre de joueurs incorrect')
    else:
        for player in data['players']:
            player_name = data['players'][player]['name']
            if int(data['players'][player]['ranking']) <= len(data['players'])/2:
                upper_group.append(player_name)
            else:
                lower_group.append(player_name)

    first_match = lower_group[0] +' against ' + upper_group[0]
    second_match = lower_group[1] +' against ' + upper_group[1]
    third_match = lower_group[2] +' against ' + upper_group[2]
    fourth_match = lower_group[3] +' against ' + upper_group[3]

    print(first_match + '\n' + second_match + '\n' + third_match + '\n' + fourth_match)




