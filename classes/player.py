from tinydb import TinyDB

class Player:
    '''Class defining a player and its attributes'''

    def __init__(self, name, firstname, date_of_birth, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking


    def save(self):
        serialized_player = {'name': self.name, 'firstname': self.firstname, 'date_of_birth': self.date_of_birth, 'gender': self.gender, 'ranking': self.ranking}
        db = TinyDB('chess.json')
        global players_table
        players_table = db.table('players')
        players_table.insert(serialized_player)
        

    #geter des infos joueur

    def get_ranking(self):
        return self.ranking


    def set_ranking(self, ranking):
        self.ranking = ranking


    def delete(self):
        #remove player
        pass
        









