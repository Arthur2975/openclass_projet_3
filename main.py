from tinydb import TinyDB
import json
from classes import player 
from classes import tournoi


def new_tournament():
    #new tournament
    new_tournament = tournoi.Tournoi(input(' New tournament: \n Tournament_s name'), input(' place'), input('date'))
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

    print(lower_group[0])
    first_match = [lower_group[0], upper_group[0]]
    second_match = [lower_group[1], upper_group[1]]
    third_match = [lower_group[2], upper_group[2]]
    fourth_match = [lower_group[3], upper_group[3]]

    input('first match : ' + first_match[0] + 'against' + first_match[1])
    input('second match : ' + second_match[0] + 'against' + second_match[1])
    input('third match : ' + third_match[0] + 'against' + third_match[1])
    input('fourth match : ' + fourth_match[0] + 'against' + fourth_match[1])

#entrer des scores

def enter_scores():
    generate_matchs()
    #creer une liste pour chaque match

# repeter generate match et enter score until the tournament's done

def main():
    new_tournament()
    new_player()
    i = 0
    while i < 4:
        input('generating match pair, press enter')
        generate_matchs()
        #enter score
        i += 1

if __name__ == '__main__':
    main()


