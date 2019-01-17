class Board:

    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []

    def add( self, piece ):
        assert( piece.is_piece() )

        if( piece.white ):
            self.white_pieces.append( piece )
        else:
            self.black_pieces.append( piece )
