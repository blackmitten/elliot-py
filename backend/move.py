from backend.square import Square

class Move:
    def __init__( self, board, start, end ):
        self.board = board
        self.start = start
        self.end = end
        self.promoted = None
        self.capturing = False

    def __str__(self):
        return str(self.start) + str(self.end)
