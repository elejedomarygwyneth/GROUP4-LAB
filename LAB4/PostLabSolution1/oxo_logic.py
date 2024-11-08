import os, random
import oxo_data

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def saveGame(self):
        oxo_data.saveGame(self.board)
    
    def restoreGame(self):
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) != 9:
                self.board = [" "] * 9
        except IOError:
            self.board = [" "] * 9
        
    def _generateMove(self):
        options = [i for i in range(9) if self.board[i] == " "]
        return random.choice(options) if options else -1
        
    def _isWinningMove(self):
        wins = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        return any(self.board[a] == self.board[b] == self.board[c] != " " for a, b, c in wins)

    def userMove(self, cell):
        if self.board[cell] != " ":
            raise ValueError("Invalid cell")
        self.board[cell] = "X"
        return "X" if self._isWinningMove() else ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return "D"
        self.board[cell] = "O"
        return "O" if self._isWinningMove() else ""

def test():
    game = Game()
    result = ""
    while not result:
        print(game.board)
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
            
    print("Draw" if result == "D" else f"Winner is: {result}")
    print(game.board)

if __name__ == "__main__":
    test()
