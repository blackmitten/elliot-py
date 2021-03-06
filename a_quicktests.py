from backend.square import Square
from backend.move import Move
from backend.move_validator import MoveValidator
import backend.pieces as pieces
import backend.board_factory as board_factory
from menzel_py.assertion import *
from menzel_py.testing import run_tests_in_class

class AQuickTests:
    @staticmethod
    def square_equality():
        s1 = Square(0, 0)
        s2 = Square(0, 1)
        s3 = Square(0, 1)
        s4 = Square(1, 1)
        s5 = Square(1, 1)
        Assert.are_equal(s1, s1)
        Assert.are_not_equal(s1, s2)
        Assert.are_equal(s2, s3)
        Assert.are_not_equal(s3, s4)
        Assert.are_equal(s4, s5)

    @staticmethod
    def square_offset():
        s6 = Square(4, 4)
        s7 = Square(2, 6)
        s8 = s6.offset(-2, 2)
        Assert.are_not_equal(s6, s7)
        Assert.are_equal(s7, s8)

    @staticmethod
    def square_copy():
        s1 = Square(1, 1)
        s2 = s1
        Assert.are_equal(s1, s2)

    @staticmethod
    def square_construct_from_notation():
        Assert.are_equal( Square.from_notation("a1"), Square(1, 1))
        Assert.are_not_equal( Square.from_notation("h1"), Square(1, 1))
        Assert.are_equal( Square.from_notation("h1"), Square(8, 1))
        Assert.are_equal( Square.from_notation("h8"), Square(8, 8))
        Assert.are_equal( Square.from_notation("a8"), Square(1, 8))

    @staticmethod
    def square_to_string():
        Assert.are_equal( str(Square.from_notation("a1")), "a1" )
        Assert.are_equal( str(Square.from_notation("h5")), "h5" )

    @staticmethod
    def square_subtraction():
        s1 = Square(2, 5)
        s2 = Square(6, 2)
        v = s1 - s2
        Assert.are_equal(v.x, -4)
        Assert.are_equal(v.y, 3)
        
    @staticmethod
    def fen_char():
        Assert.are_equal( pieces.Pawn( Square(2,2), True).fen_char(), "P" )
        Assert.are_equal( pieces.Pawn( Square(2,2), False).fen_char(), "p" )
        Assert.are_equal( pieces.Rook( Square(2,2), True).fen_char(), "R" )
        Assert.are_equal( pieces.Rook( Square(2,2), False).fen_char(), "r" )
        Assert.are_equal( pieces.Bishop( Square(2,2), True).fen_char(), "B" )
        Assert.are_equal( pieces.Bishop( Square(2,2), False).fen_char(), "b" )
        Assert.are_equal( pieces.Knight( Square(2,2), True).fen_char(), "N" )
        Assert.are_equal( pieces.Knight( Square(2,2), False).fen_char(), "n" )
        Assert.are_equal( pieces.King( Square(2,2), True).fen_char(), "K" )
        Assert.are_equal( pieces.King( Square(2,2), False).fen_char(), "k" )
        Assert.are_equal( pieces.Queen( Square(2,2), True).fen_char(), "Q" )
        Assert.are_equal( pieces.Queen( Square(2,2), False).fen_char(), "q" )

    @staticmethod
    def init_new_board():
        board = board_factory.BoardFactory.init_new_game()
        board_fen = board.get_fen_string()
        starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        Assert.are_equal( board_fen, starting_fen)


    @staticmethod
    def reject_invalid_moves():
        board = board_factory.BoardFactory.init_new_game()
        validator = MoveValidator()

        move = Move( board, Square.from_notation( "e1" ), Square.from_notation( "e1" ) )
        Assert.is_false( validator.validate( move ), "MoveValidator should reject move with start and end square the same" )

        move = Move( board, Square.from_notation( "e3" ), Square.from_notation( "e4" ) )
        Assert.is_false( validator.validate( move ), "MoveValidator should reject move from unoccupied square" )

        move = Move( board, Square.from_notation( "e7" ), Square.from_notation( "e6" ) )
        Assert.is_false( validator.validate( move ), "MoveValidator should reject black move when it's white's turn" )

        move = Move( board, Square.from_notation( "e2" ), Square.from_notation( "e3" ) )
        Assert.is_true( validator.validate( move ), "MoveValidator should allow white pawn moving one space" )

        move = Move( board, Square.from_notation( "e2" ), Square.from_notation( "e5" ) )
        Assert.is_false( validator.validate( move ), "MoveValidator should reject pawn moving three spaces" )

run_tests_in_class(AQuickTests)

