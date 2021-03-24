from tinydb import TinyDB

class Player:
    '''Class defining a player and its attributes'''

    def __init__(self, name, firstname, date_of_birth, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking


    def save(player):
        serialized_player = {'name': player.name, 'firstname': player.firstname, 'date_of_birth': player.date_of_birth, 'gender': player.gender, 'ranking': player.ranking}
        db = TinyDB('players.json')
        db.insert(serialized_player)


    #geter des infos joueur

    def get_ranking(self):
        return self.ranking


    def set_ranking(self, ranking):
        self.ranking = ranking


    def delete(self):
        #remove player
        pass
        









