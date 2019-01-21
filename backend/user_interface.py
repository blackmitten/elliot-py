from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def waiting_for_black_human( self, b ):
        pass

    @abstractmethod
    def waiting_for_white_human( self, b ):
        pass

    @abstractmethod
    def wait_for_human( self ):
        pass

