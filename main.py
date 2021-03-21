from tinydb import TinyDB




class Player:
    '''Class defining a player and its attributes'''

    def __init__(self, name, firstname, date_of_birth, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking


    def add_player_to_json(player):
        serialized_player = {'name': player.name, 'firstname': player.firstname, 'date_of_birth': player.date_of_birth, 'gender': player.gender, 'ranking': player.ranking}
        db = TinyDB('players.json')
        db.insert(serialized_player)


    def getranking(self):
        return self.ranking


    def setranking(self, ranking):
        self.ranking = ranking


def main():
    player_1 = Player(input('nom'), input('prenom'), input('date_of_birth'), input('gender'), input('ranking'))
    


if __name__ == '__main__' :
    main()



'''
    def update_player():
        pass

    def delete_player():
        pass
'''





