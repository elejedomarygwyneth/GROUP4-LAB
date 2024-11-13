import random
import oxo_data
import unittest

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def save(self):
        oxo_data.saveGame(self.board)

    def restore(self):
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) != 9:
                self.board = [" "] * 9
        except IOError:
            self.board = [" "] * 9

    def _generateMove(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def _isWinningMove(self):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.board[cell] != ' ':
            raise ValueError("Invalid cell")
        self.board[cell] = 'X'
        return 'X' if self._isWinningMove() else ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        return 'O' if self._isWinningMove() else ""

def play_game():
    game = Game()
    result = ""
    while not result:
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
        if result == 'D':
            print("It's a draw")
        elif result:
            print("Winner is:", result)
    return result

class TestGame(unittest.TestCase):
    def test_result(self):
        result = play_game()
        self.assertIn(result, ['X', 'O', 'D'])

if __name__ == "__main__":
    play_game()
    unittest.main()
