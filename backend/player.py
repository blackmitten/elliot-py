from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def human():
        pass

    @abstractmethod
    def white():
        pass

    @abstractmethod
    def name():
        pass
    
    @abstractmethod
    def play( board ):
        pass
    
