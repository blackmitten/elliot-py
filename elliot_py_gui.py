import tkinter
from draw_pieces_badly import *
from backend.board_factory import BoardFactory

class ElliotPyGui:
    def new_game(self):
        self.board = BoardFactory.init_new_game()
        self.draw_pieces_badly.draw( self.board_control, self.board )
        

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.menubar = tkinter.Label(master, text="This is where the menu bar will be")
        self.menubar.grid(row=0,columnspan=2, sticky=tkinter.W)

        self.board_control = tkinter.Canvas(master, width=400, height=400)
        self.board_control.grid(row=1)

        self.close_button = tkinter.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2, columnspan=2)

        self.draw_pieces_badly = DrawPiecesBadly()

        self.new_game()

    def greet(self):
        print("Greetings!")

root = tkinter.Tk()
my_gui = ElliotPyGui(root)
root.mainloop()