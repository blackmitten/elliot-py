from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def IsKing(self):
        pass
    @abstractmethod
    def IsRook(self):         
        pass
    @abstractmethod
    def IsPawn(self):         
        pass
    @abstractmethod
    def IsQueen(self):         
        pass
    @abstractmethod
    def IsBishop(self):         
        pass
    @abstractmethod
    def IsKnight(self):         
        pass
    @abstractmethod
    def Accept(self, visitor):         
        pass

    def IsDiagonalMover(self):
        return IsDiagonalMover(self)
    def IsStraightMover(self):         
        return IsStraightMover(self)
    

class PieceVisitor(ABC):
    @abstractmethod
    def VisitPawn(self):         
        pass
    @abstractmethod
    def VisitKing(self):         
        pass
    @abstractmethod
    def VisitRook(self):         
        pass
    @abstractmethod
    def VisitQueen(self):         
        pass
    @abstractmethod
    def VisitBishop(self):         
        pass
    @abstractmethod
    def VisitKnight(self):         
        pass

def IsDiagonalMover(piece):
    return piece.IsBishop() or piece.IsQueen()

def IsStraightMover(piece):         
    return piece.IsRook() or piece.IsQueen()

class Pawn(Piece):
    def __init__(self, white):
        self.white=white

    def IsKing(self):
        return False
    def IsRook(self):         
        return False
    def IsPawn(self):         
        return True
    def IsQueen(self):         
        return False
    def IsBishop(self):         
        return False
    def IsKnight(self):         
        return False
    def Accept(self, visitor):
        return visitor.VisitPawn(self)

class King(Piece):
    def __init__(self, white):
        self.white=white

    def IsKing(self):
        return True
    def IsRook(self):         
        return False
    def IsPawn(self):         
        return False
    def IsQueen(self):         
        return False
    def IsBishop(self):         
        return False
    def IsKnight(self):         
        return False
    def Accept(self, visitor):
        return visitor.VisitKing(self)

class Rook(Piece):
    def __init__(self, white):
        self.white=white

    def IsKing(self):
        return False
    def IsRook(self):         
        return True
    def IsPawn(self):         
        return False
    def IsQueen(self):         
        return False
    def IsBishop(self):         
        return False
    def IsKnight(self):         
        return False
    def Accept(self, visitor):
        return visitor.VisitRook(self)

class Queen(Piece):
    def __init__(self, white):
        self.white=white

    def IsKing(self):
        return False
    def IsRook(self):         
        return False
    def IsPawn(self):         
        return False
    def IsQueen(self):         
        return True
    def IsBishop(self):         
        return False
    def IsKnight(self):         
        return False
    def Accept(self, visitor):
        return visitor.VisitQueen(self)

class Bishop(Piece):
    def __init__(self, white):
        self.white=white

    def IsKing(self):
        return False
    def IsRook(self):         
        return False
    def IsPawn(self):         
        return False
    def IsQueen(self):         
        return False
    def IsBishop(self):         
        return True
    def IsKnight(self):         
        return False
    def Accept(self, visitor):
        return visitor.VisitBishop(self)

class Knight(Piece):
    def __init__(self, white):
        self.white=white

    def IsKing(self):
        return False
    def IsRook(self):         
        return False
    def IsPawn(self):         
        return False
    def IsQueen(self):         
        return False
    def IsBishop(self):         
        return False
    def IsKnight(self):         
        return True
    def Accept(self, visitor):
        return visitor.VisitKnight(self)

