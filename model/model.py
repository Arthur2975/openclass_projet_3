from tinydb import TinyDB


db = TinyDB('chess.json')


class Model:
    '''database model class'''

    def __init__(self):
        self.db = db.all()
