from backend.options import Options
from backend.square import Square

class MoveValidator:
    def __init__( self ):
        self.valid = None


    def validate( self, move ):
        if ( move.start == move.end ):
            return False
        self.valid = None

        piece = move.board.get_piece_on_square( move.start )
        if piece is None:
            return False
        if piece.white != move.board.whites_turn:
            return False

        piece.accept(self, move);

        if Options.diagnostic_mode:
            pass


        return self.valid

        '''

#if DIAGNOSTIC
            string fenBefore = move.Board.GetFenString();
#endif
            var undo = new Undo();
            move.Board.Move(move, false, undo);
#if DIAGNOSTIC
            string fenAfter = move.Board.GetFenString();
#endif
            if (move.Board.CurrentPlayerInCheck)
            {
                _valid = false;
            }
            move.Board.UndoLastmove(undo);
#if DIAGNOSTIC
            string fenAfterUndo = move.Board.GetFenString();
            Assert.IsTrue(fenBefore != fenAfter);
            Assert.IsTrue(fenBefore == fenAfterUndo);
#endif
            return _valid.Value;
'''

    def visit_pawn(self, pawn, move):
        board = move.board
        direction = 1 if pawn.white else -1
        dx = move.end.x - move.start.x
        dy = move.end.y - move.start.y
        squares_advanced = dy * direction

        self.valid = True
        if dx == 0:
            if squares_advanced == 1:
                if not board.get_piece_on_square( move.end ) is None:
                    self.valid = False
            elif squares_advanced == 2:
                if not board.get_piece_on_square( Square( move.start.x, move.start.y + direction)) is None:
                    self.valid = False
                elif not board.get_piece_on_square( move.end ) is None:
                    self.valid = False
            else:
                self.valid = False
        elif abs(dx) == 1 and squares_advanced == 1:
            captured_piece = board.get_piece_on_square( move.end )
            if board.en_passant_target == move.end:
                captured_piece = board.get_piece_on_square(board.en_passant_target.offset( 0, -direction ))
            if captured_piece is None:
                self.valid = False
            elif captured_piece.white == pawn.white:
                self.valid = False
            else:
                move.capturing = True
        else:
            self.valid = False
