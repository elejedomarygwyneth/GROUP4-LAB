import os

game_file = "oxogame.dat"

def _getPath():
    try:
        game_path = os.environ.get('HOMEPATH') or os.environ.get('HOME')
        if not game_path or not os.path.exists(game_path):
            game_path = os.getcwd()
    except KeyError:
        game_path = os.getcwd()
    return game_path

def saveGame(game):
    path = os.path.join(_getPath(), game_file)
    with open(path, 'w') as gf:
        gf.write(''.join(game))

def restoreGame():
    path = os.path.join(_getPath(), game_file)
    with open(path) as gf:
        return list(gf.read())

def test():
    print("Path =", _getPath())
    saveGame(list("XO XO XO "))
    print(restoreGame())

if __name__ == "__main__":
    test()

