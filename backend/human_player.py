from backend.player import Player

class HumanPlayer(Player):
    def __init__( self, white, user_interface ):
        self.__white=white
        self.__user_interface = user_interface

    def human(self):
        return True

    def white(self):
        return self.__white

    def name(self):
        return "Human"
    
    def play( self, board ):
        self.__user_interface.waiting_for_black_human = not self.__white
        self.__user_interface.waiting_for_white_human = self.__white
        return self.__user_interface.wait_for_human()
    
