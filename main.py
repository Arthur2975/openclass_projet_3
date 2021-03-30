from tinydb import TinyDB, Query
import json
from classes import player as play
from classes import tournoi as tour


db = TinyDB('chess.json')


def new_tournament():
    #new tournament
    new_tournament = tour.Tournoi(input(' New tournament: \n Tournament_s name'), input(' place'), input('date'))
    tour.Tournoi.save(new_tournament)


def new_player():
    #new players
    continue_while = True
    
    while continue_while == True:
        add_player = input('Do you want to add a new player? : Y/N')
        if add_player.lower() != 'y':
            break
        else:
            new_player = play.Player(input('name: '), input('firstname: '), input('date_of_birth: '), input('gender: '), input('ranking: '))

        play.Player.save(new_player)
    

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
        match()
        i += 1


def match():
    
    table_player = db.table('players')
    all_players = table_player.all()

    list_player = []
    for player in all_players:
        list_player.append(play.Player(player['name'], player['firstname'], player['date_of_birth'], player['gender'], player['ranking']))
    
    sorted_list_player = sorted(list_player, key=lambda player: player.ranking)

    upper_group = []
    lower_group = []

    upper_group.append(sorted_list_player[:4])
    lower_group.append(sorted_list_player[4:7])

    for player in upper_group:
        print(dir(player))
        
        

    

    '''
    if len(all_players) != 8:
        print('incorrect number of players')
        return None

    if int(self.ranking) < len(db)/2:
        upper_group.append(self)
    elif self.ranking > 8:
        lower_group.append(self)
    #first match
    print('first_match : ' + upper_group[0] + ' against ' + lower_group[0])
    #enter scores:
    score_1 = input('Enter ' + upper_group[0] + 's' + ' score')
    score_2 = input('Enter ' + lower_group[0] + 's' + ' score')
    first_match = (upper_group[0], score_1, lower_group[0], score_2)
    #second match
    print('second match : ' + upper_group[1] + 'against' + lower_group[1])
    #enter scores:
    score_3 = input('Enter ' + upper_group[1] + 's' + ' score')
    score_4 = input('Enter ' + lower_group[1] + 's' + ' score')
    second_match = (upper_group[1], score_3, lower_group[1], score_4)   
    #third match 
    print('third_match : ' + upper_group[2] + 'against' + lower_group[2])
    #Enter scores:
    score_5 = input('Enter ' + upper_group[2] + 's' + ' score')
    score_6 = input('Enter ' + lower_group[2] + 's' + ' score')
    third_match = (upper_group[2], score_5, lower_group[2], score_6)  
    #fourth match
    print('fourth_match : ' + upper_group[3] + 'against' + lower_group[3])
    #Enter scores:
    score_7 = input('Enter ' + upper_group[3] + 's' + ' score')
    score_8 = input('Enter ' + lower_group[3] + 's' + ' score')
    fourth_match = (upper_group[3], score_7, lower_group[3], score_8)  

    list_of_the_round = [first_match, second_match, third_match, fourth_match]
    '''


# if __name__ == '__main__':
#     main()


#d'abord trier la liste de joueurs
#ensuite utiliser [0:3] pour prendre les prenmiers de la liste et depuis la fin pour les 4 derniers

match()