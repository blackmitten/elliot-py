from backend.pieces import PieceVisitor

class FenCharPieceVisitor(PieceVisitor):
    def visit_pawn(self, pawn):         
        return 'P' if pawn.white else 'p'
    def visit_king(self, king):         
        return 'K' if king.white else 'k'
    def visit_rook(self, rook):         
        return 'R' if rook.white else 'r'
    def visit_queen(self, queen):         
        return 'Q' if queen.white else 'q'
    def visit_bishop(self, bishop):         
        return 'B' if bishop.white else 'b'
    def visit_knight(self, knight):         
        return 'N' if knight.white else 'n'

