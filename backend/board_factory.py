from backend.board import Board
import backend.pieces as pieces
from backend.square import Square

class BoardFactory:
    @staticmethod
    def init_new_game():
        board = Board()
        for x in range(1, 9):
            board.add( pieces.Pawn( Square(x, 7), False ) )
            board.add( pieces.Pawn( Square(x, 2), True ) )
        board.add( pieces.Rook( Square(1, 8), False ) )
        board.add( pieces.Rook( Square(8, 8), False ) )
        board.add( pieces.Knight( Square(2, 8), False ) )
        board.add( pieces.Knight( Square(7, 8), False ) )
        board.add( pieces.Bishop( Square(3, 8), False ) )
        board.add( pieces.Bishop( Square(6, 8), False ) )
        board.add( pieces.Queen( Square(4, 8), False ) )
        board.add( pieces.King( Square(5, 8), False ) )

        board.add( pieces.Rook( Square(1, 1), True ) )
        board.add( pieces.Rook( Square(8, 1), True ) )
        board.add( pieces.Knight( Square(2, 1), True ) )
        board.add( pieces.Knight( Square(7, 1), True ) )
        board.add( pieces.Bishop( Square(3, 1), True ) )
        board.add( pieces.Bishop( Square(6, 1), True ) )
        board.add( pieces.Queen( Square(4, 1), True ) )
        board.add( pieces.King( Square(5, 1), True ) )

        board.white_can_castle_kingside = True
        board.white_can_castle_queenside = True
        board.black_can_castle_kingside = True
        board.black_can_castle_queenside = True

        board.whites_turn = True

        return board

