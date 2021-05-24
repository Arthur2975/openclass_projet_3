from tinydb import TinyDB
from controller import controller

db = TinyDB('chess.json')


def main():
    '''main'''
    tournament = ""
    ctrl = controller.Controller(tournament)
    ctrl.menu()


if __name__ == '__main__':
    main()


# retourner au menu entre tous les rounds
# lier les joueurs au tournoi dans bd
# stocker les score de chaque match et chaque match adversaires dans la bd

# load les tournoi et creer les instances

# modif les import de modules, ex; from model.round import Round
