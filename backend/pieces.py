from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def is_king(self):
        pass
    @abstractmethod
    def is_rook(self):         
        pass
    @abstractmethod
    def is_pawn(self):         
        pass
    @abstractmethod
    def is_queen(self):         
        pass
    @abstractmethod
    def is_bishop(self):         
        pass
    @abstractmethod
    def is_knight(self):         
        pass
    @abstractmethod
    def accept(self, visitor):         
        pass
    @abstractmethod
    def fen_char(self):
        pass

    def is_diagonal_mover(self):
        return is_diagonal_mover(self)
    def is_straight_mover(self):         
        return is_straight_mover(self)

    def is_piece(self):
        return True
    

class PieceVisitor(ABC):
    @abstractmethod
    def visit_pawn(self, data):         
        pass
    @abstractmethod
    def visit_king(self, data):         
        pass
    @abstractmethod
    def visit_rook(self, data):         
        pass
    @abstractmethod
    def visit_queen(self, data):         
        pass
    @abstractmethod
    def visit_bishop(self, data):         
        pass
    @abstractmethod
    def visit_knight(self, data):         
        pass

def is_diagonal_mover(piece):
    return piece.is_bishop() or piece.is_queen()

def is_straight_mover(piece):         
    return piece.is_rook() or piece.is_queen()

class Pawn(Piece):
    def __init__(self, pos, white):
        self.white=white
        self.pos=pos

    def is_king(self):
        return False
    def is_rook(self):         
        return False
    def is_pawn(self):         
        return True
    def is_queen(self):         
        return False
    def is_bishop(self):         
        return False
    def is_knight(self):         
        return False
    def accept(self, visitor, data):
        return visitor.visit_pawn(self, data)
    def fen_char(self):
        return "P" if self.white else "p"

class King(Piece):
    def __init__(self, pos, white):
        self.white=white
        self.pos=pos

    def is_king(self):
        return True
    def is_rook(self):         
        return False
    def is_pawn(self):         
        return False
    def is_queen(self):         
        return False
    def is_bishop(self):         
        return False
    def is_knight(self):         
        return False
    def accept(self, visitor, data):
        return visitor.visit_king(self, data)
    def fen_char(self):
        return "K" if self.white else "k"

class Rook(Piece):
    def __init__(self, pos, white):
        self.white=white
        self.pos=pos

    def is_king(self):
        return False
    def is_rook(self):         
        return True
    def is_pawn(self):         
        return False
    def is_queen(self):         
        return False
    def is_bishop(self):         
        return False
    def is_knight(self):         
        return False
    def accept(self, visitor, data):
        return visitor.visit_rook(self, data)
    def fen_char(self):
        return "R" if self.white else "r"

class Queen(Piece):
    def __init__(self, pos, white):
        self.white=white
        self.pos=pos

    def is_king(self):
        return False
    def is_rook(self):         
        return False
    def is_pawn(self):         
        return False
    def is_queen(self):         
        return True
    def is_bishop(self):         
        return False
    def is_knight(self):         
        return False
    def accept(self, visitor, data):
        return visitor.visit_queen(self, data)
    def fen_char(self):
        return "Q" if self.white else "q"

class Bishop(Piece):
    def __init__(self, pos, white):
        self.white=white
        self.pos=pos

    def is_king(self):
        return False
    def is_rook(self):         
        return False
    def is_pawn(self):         
        return False
    def is_queen(self):         
        return False
    def is_bishop(self):         
        return True
    def is_knight(self):         
        return False
    def accept(self, visitor, data):
        return visitor.visit_bishop(self, data)
    def fen_char(self):
        return "B" if self.white else "b"

class Knight(Piece):
    def __init__(self, pos, white):
        self.white=white
        self.pos=pos

    def is_king(self):
        return False
    def is_rook(self):         
        return False
    def is_pawn(self):         
        return False
    def is_queen(self):         
        return False
    def is_bishop(self):         
        return False
    def is_knight(self):         
        return True
    def accept(self, visitor, data):
        return visitor.visit_knight(self, data)
    def fen_char(self):
        return "N" if self.white else "n"

