import os

game_file = "oxogame.dat"

def _getPath():
    try:
        game_path = os.environ.get('HOMEPATH') or os.environ.get('HOME')
        if not game_path or not os.path.exists(game_path):
            game_path = os.getcwd()
    except (KeyError, TypeError):
        game_path = os.getcwd()
    return game_path

def saveGame(game):
    path = os.path.join(_getPath(), game_file)
    try:
        with open(path, 'w') as gf:
            gf.write(''.join(game))
    except FileNotFoundError:
        print("Failed to save file")

def restoreGame():
    path = os.path.join(_getPath(), game_file)
    with open(path) as gf:
        return list(gf.read())
