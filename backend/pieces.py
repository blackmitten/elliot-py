from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def IsKing(self):
        pass

class Pawn(Piece):
    def IsKing(self):
        return False

class King(Piece):
    def IsKing(self):
        return True



p = Pawn()
k = King()
