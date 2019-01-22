import tkinter
from draw_pieces_badly import DrawPiecesBadly

class BoardControl:

    def __init__( self, master ):
        self.canvas = tkinter.Canvas(master, width=400, height=400)
        self.__draw_pieces_badly = DrawPiecesBadly()

    def draw( self, board ):
        self.__draw_pieces_badly.draw( self.canvas, board )

        
