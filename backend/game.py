from _thread import start_new_thread
from enum import Enum
import time

class GameState(Enum):
    in_play = 0
    stale_mate = 1
    white_wins = 2
    black_wins = 3
    abandoned = 4

class Game:
    def __init__( self,  white_player, black_player, board ):
        self.__white_player = white_player
        self.__black_player = black_player
        self.__board = board
        self.game_state = GameState.in_play

    def start_play( self ):
        start_new_thread( self.play )
        

    def play( self ):
        i = 0
        while self.game_state == GameState.in_play:
            self.play_single_move()

    def play_single_move( self ):
        move = None


