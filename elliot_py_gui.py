import tkinter
from draw_pieces_badly import DrawPiecesBadly
from backend.board_factory import BoardFactory
from backend.human_player import HumanPlayer
from backend.game import Game
from backend.user_interface import UserInterface

class ElliotPyGui(UserInterface):
    def new_game(self):
        self.board = BoardFactory.init_new_game()
        white_player = HumanPlayer( True, self )
        black_player = HumanPlayer( False, self )
        self.__draw_pieces_badly.draw( self.board_control, self.board )
        self.__game = Game( white_player, black_player, self.board )
        self.__game.start_play()

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.menubar = tkinter.Label(master, text="This is where the menu bar will be")
        self.menubar.grid(row=0,columnspan=2, sticky=tkinter.W)

        self.board_control = tkinter.Canvas(master, width=400, height=400)
        self.board_control.grid(row=1)

        self.close_button = tkinter.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, columnspan=2)

        self.__draw_pieces_badly = DrawPiecesBadly()

        self.new_game()

    def greet(self):
        print("Greetings!")

    def waiting_for_black_human( self, b ):
        pass

    def waiting_for_white_human( self, b ):
        pass

    def wait_for_human( self ):
        pass



root = tkinter.Tk()
my_gui = ElliotPyGui(root)
root.mainloop()