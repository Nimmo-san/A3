

class Game:

    def create_board(self):
        board = []
        for i in range(self.size):
            board.append([])
            for j in range(self.size):
                board[i].append(i + j)
        return board

    def __init__(self):
        self.size = 8
