from tinydb import TinyDB
from controller import controller

db = TinyDB('chess.json')


def main():
    '''main'''
    ctrl = controller.Controller()
    ctrl.main_menu()


if __name__ == '__main__':
    main()


# controller les input, 1 ou 0, 0,5 rien d'autre
# rajouter un attribut à la classe tournoi avec liste des joueurs, les tours et les matchs
# rajouter serializer les match dans def match
# generer un rapport html de flake 8 -> module flake 8 html
