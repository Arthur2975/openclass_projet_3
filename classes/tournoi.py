from tinydb import TinyDB

class Tournoi:

    NUMBER_OF_TOURS = 4
    instances_list = []
    players_lit = []

    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date

    def getdate(self):
        return self.date

    def setdate(self, date):
        self.date = date
    
    def time_control():
        #time control
        pass

    def add_comment():
        #write director's comment
        pass

    def save(tournament):
        serialized_tournament = {'name': tournament.name, 'place': tournament.place, 'date': tournament.date}
        db = TinyDB('tournaments.json')
        db.insert(serialized_tournament)
    
  




