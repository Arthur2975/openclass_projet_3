from tinydb import TinyDB, Query


class round:
    def __init__(self, name, date, hour):
        self.name = name
        self.date = date
        self.hour = hour
        self.first_match = []

    def add_match(self):
        pass
        # un peu comme un setter


# un attribut numéro pour le round
# si le n° est 1 alors generation de paires 1er round....
