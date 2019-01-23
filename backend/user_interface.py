from abc import ABC, abstractmethod

class UserInterface(ABC):
    @property
    @abstractmethod
    def waiting_for_black_human( self ):
        pass

    @property
    @abstractmethod
    def waiting_for_white_human( self ):
        pass

    @abstractmethod
    def wait_for_human( self ):
        pass

