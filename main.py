from tinydb import TinyDB
from controller import controller

db = TinyDB('chess.json')


def main():
    '''main fonction creating an instance of controller'''
    tournament = ""
    ctrl = controller.Controller(tournament)
    ctrl.menu()


if __name__ == '__main__':
    main()
