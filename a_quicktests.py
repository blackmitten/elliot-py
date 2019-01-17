from backend.square import Square
from backend.fen_char_piece_visitor import FenCharPieceVisitor
import backend.pieces as pieces
import backend.board_factory as board_factory

class AQuickTests:
    @staticmethod
    def square_equality():
        s1 = Square(0, 0)
        s2 = Square(0, 1)
        s3 = Square(0, 1)
        s4 = Square(1, 1)
        s5 = Square(1, 1)
        assert(s1==s1)
        assert(s1!=s2)
        assert(s2==s3)
        assert(s3!=s4)
        assert(s4==s5)

    @staticmethod
    def square_offset():
        s6 = Square(4, 4)
        s7 = Square(2, 6)
        s8 = s6.offset(-2, 2)
        assert(s6 != s7)
        assert(s7 == s8)

    @staticmethod
    def square_copy():
        s1 = Square(1, 1)
        s2 = s1
        assert(s1==s2)

    @staticmethod
    def square_construct_from_notation():
        assert( Square.from_notation("a1") == Square(1, 1))
        assert( Square.from_notation("h1") != Square(1, 1))
        assert( Square.from_notation("h1") == Square(8, 1))
        assert( Square.from_notation("h8") == Square(8, 8))
        assert( Square.from_notation("a8") == Square(1, 8))

    @staticmethod
    def square_to_string():
        assert( str(Square.from_notation("a1")) == "a1" )
        assert( str(Square.from_notation("h5")) == "h5" )

    @staticmethod
    def square_subtraction():
        s1 = Square(2, 5)
        s2 = Square(6, 2)
        v = s1 - s2
        assert(v.x == -4)
        assert(v.y == 3)
        
    @staticmethod
    def fen_char():
        visitor = FenCharPieceVisitor()
        assert( pieces.Pawn( Square(2,2), True).accept( visitor ) == "P" )
        assert( pieces.Pawn( Square(2,2), False).accept( visitor ) == "p" )
        assert( pieces.Rook( Square(2,2), True).accept( visitor ) == "R" )
        assert( pieces.Rook( Square(2,2), False).accept( visitor ) == "r" )
        assert( pieces.Bishop( Square(2,2), True).accept( visitor ) == "B" )
        assert( pieces.Bishop( Square(2,2), False).accept( visitor ) == "b" )
        assert( pieces.Knight( Square(2,2), True).accept( visitor ) == "N" )
        assert( pieces.Knight( Square(2,2), False).accept( visitor ) == "n" )
        assert( pieces.King( Square(2,2), True).accept( visitor ) == "K" )
        assert( pieces.King( Square(2,2), False).accept( visitor ) == "k" )
        assert( pieces.Queen( Square(2,2), True).accept( visitor ) == "Q" )
        assert( pieces.Queen( Square(2,2), False).accept( visitor ) == "q" )

    @staticmethod
    def init_new_board():
        board = board_factory.BoardFactory.init_new_game()
        board_fen = board.get_fen_string()
        starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        assert( board_fen == starting_fen)



methods = [name for name in dir(AQuickTests) if callable(getattr(AQuickTests, name)) if not name.startswith('_')]
for method in methods:
    print(method)
    getattr(AQuickTests, method)()

print("All tests done")
