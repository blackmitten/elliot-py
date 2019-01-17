from backend.board import *
from backend.pieces import *
from backend.square import *

class BoardFactory:
    @staticmethod
    def init_new_game():
        board = Board()
        board.add( Pawn( Square(1,1), True ) )