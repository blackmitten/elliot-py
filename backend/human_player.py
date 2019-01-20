from backend.player import Player

class HumanPlayer(Player):
    def __init__(self, white):
        self.__white=white

    def human(self):
        return True

    def white(self):
        return self.__white

    def name(self):
        return "Human"
    
    def play( self, board ):
        pass
    
