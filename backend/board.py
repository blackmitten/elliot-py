from backend.fen_char_piece_visitor import FenCharPieceVisitor
from backend.square import Square

class Board:

    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []
        self.white_can_castle_kingside = None
        self.white_can_castle_queenside = None
        self.black_can_castle_kingside = None
        self.black_can_castle_queenside = None
        self.en_passant_target = None
        self.half_move_clock = 0
        self.full_move_clock = 1
        self.squares = [[None for x in range(8)] for y in range(8)]
        self.white_king = None
        self.black_king = None
        self.whites_turn = None

    def add( self, piece ):
        assert( piece.is_piece() )

        if( piece.white ):
            self.white_pieces.append( piece )
            if piece.is_king():
                if( self.white_king is not None ):
                    raise RuntimeError("Already have a white king")
                self.white_king = piece
        else:
            self.black_pieces.append( piece )
            if piece.is_king():
                if( self.black_king is not None ):
                    raise RuntimeError("Already have a black king")
                self.black_king = piece

        self.squares[ piece.pos.x - 1][piece.pos.y - 1 ] = piece

    def get_piece_on_square( self, square, suppress_out_of_bounds_error = False ):
        if not square.in_bounds():
            if suppress_out_of_bounds_error:
                return None
            else:
                raise RuntimeError("Out of bounds square")
        return self.squares[square.x - 1][square.y - 1]

    def get_fen_string( self ):
        fen = ""
        fen_visitor = FenCharPieceVisitor()

        for y in range(8, 0, -1):
            x = 1
            empty_squares = 0
            while x <= 8:
                piece = self.get_piece_on_square( Square(x, y) )
                if piece is not None:
                    if empty_squares > 0:
                        fen += str( empty_squares )
                        empty_squares = 0
                    fen_char = piece.accept( fen_visitor )
                    fen += fen_char
                else:
                    empty_squares += 1
                x += 1
            if empty_squares > 0:
                fen += str( empty_squares )
                empty_squares = 0
            if y > 1:
                fen += "/"
        
        fen += ( " w " if self.whites_turn else " b " )

        if self.white_can_castle_kingside:
            fen += "K"
        if self.white_can_castle_queenside:
            fen += "Q"
        if self.black_can_castle_kingside:
            fen += "k"
        if self.black_can_castle_queenside:
            fen += "q"
        if not self.white_can_castle_kingside and not self.white_can_castle_queenside and \
           not self.black_can_castle_kingside and not self.black_can_castle_queenside:
            fen += "-"
        fen += " "
        if self.en_passant_target is not None and self.en_passant_target.in_bounds():
            fen += self.en_passant_target
        else:
            fen += "-"
        fen += " "
        fen += str(self.half_move_clock)
        fen += " "
        fen += str(self.full_move_clock)
        return fen

