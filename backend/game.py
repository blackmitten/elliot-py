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
        board = self.__board
        move = None
        if board.half_move_clock > 50:
            self.game_state = GameState.stale_mate
        if board.whites_turn:
            if board.white_can_move():
                if not self.__white_player.human:
                    pass
                    #self.__user_interface.machine_thinking = True
                #move = self.__white_player.Play( board )
            elif board.white_in_check():
                self.game_state = GameState.black_wins
            else:
                self.game_state = GameState.stale_mate
            #self.__user_interface.machine_thinking = False
        else:
            if board.black_can_move():
                if not self.__black_player.human:
                    pass
                    #self.__user_interface.machine_thinking = True
                #move = self.__black_player.Play( board )
            elif board.black_in_check():
                self.game_state = GameState.white_wins
            else:
                self.game_state = GameState.stale_mate
            #self.__user_interface.machine_thinking = False
        '''
            if (!_applicationClosing)
            {
                _userInterface.Redraw();
            }
            if (GameState == GameState.InPlay)
            {
                _log.Write(move.ToLongString());
                _userInterface.WaitForInstructionToMove();
                try
                {
                    _moveValidator.Validate(move);
                    var undo = new Undo();
#if DIAGNOSTIC
                    string fenBefore = _board.GetFenString();

                    _board.Move(move, true, undo);
                    string fenAfter = _board.GetFenString();
                    _board.CheckIntegrity();
                    Assert.IsTrue(fenBefore != fenAfter);

                    _board.UndoLastmove( undo );
                    string fenAfterUndo = _board.GetFenString();
                    _board.CheckIntegrity();
                    Assert.IsTrue(fenBefore == fenAfterUndo);

                    _board.Move(move, true, undo);
                    string fenAfterAgain = _board.GetFenString();
                    _board.CheckIntegrity();
                    Assert.IsTrue(fenAfter == fenAfterAgain);
#else
                    _board.Move(move, true, undo);
                    _board.CheckIntegrity();
#endif
                }
                catch (InvalidMoveException e)
                {
                    _userInterface.InvalidMove(e.Message);
                }

                _userInterface.Redraw();
            }
         '''

