from pieces import *

class FenCharPieceVisitor(PieceVisitor):
    def VisitPawn(self, pawn):         
        return 'P' if pawn.white else 'p'
    def VisitKing(self, king):         
        return 'K' if king.white else 'k'
    def VisitRook(self, rook):         
        return 'R' if rook.white else 'r'
    def VisitQueen(self, queen):         
        return 'Q' if queen.white else 'q'
    def VisitBishop(self, bishop):         
        return 'B' if bishop.white else 'b'
    def VisitKnight(self, knight):         
        return 'N' if knight.white else 'n'

