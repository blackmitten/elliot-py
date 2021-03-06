import tkinter
from draw_pieces_badly import DrawPiecesBadly
from backend.square import Square
from backend.move import Move
from backend.move_validator import MoveValidator
import math
from threading import Event

class BoardControl:

    def __init__( self, master ):
        self.__width = 400
        self.__square_width = self.__width / 8
        self.canvas = tkinter.Canvas(master, width=self.__width, height=self.__width)
        self.canvas.bind("<Button-1>", self.board_clicked)
        self.__draw_pieces_badly = DrawPiecesBadly()
        self.waiting_for_black_human = False
        self.waiting_for_white_human = False
        self.__move_start_square = Square( 0, 0 )
        self.human_moved = Event()
        self.board = None

    def board_clicked(self, event):
        x = 1 + math.floor( event.x / self.__square_width )
        y = 8 - math.floor( event.y / self.__square_width )
        s = Square( x, y )
        self.square_clicked( s )

    def square_clicked( self, clicked_square ):
        print( "Clicked " + str( clicked_square ) )
        if clicked_square.in_bounds():
            if self.waiting_for_black_human or self.waiting_for_white_human:
                if not self.__move_start_square.in_bounds():
                    clicked_piece = self.board.get_piece_on_square( clicked_square )
                    if not clicked_piece == None:
                        click_valid = ( clicked_piece.white and self.waiting_for_white_human ) or \
                           ( not clicked_piece.white and self.waiting_for_black_human )
                        if click_valid:
                            self.__move_start_square = clicked_square
                else:
                    self.humans_move = Move( self.board, self.__move_start_square, clicked_square )
                    self.__move_start_square = Square(0, 0)
                    move_validator = MoveValidator()
                    if move_validator.validate( self.humans_move ):
                        print( "Human moved " + str( self.humans_move ) )
                        self.human_moved.set()
        self.draw()



    def draw( self ):
        if ( self.board != None ):
            self.__draw_pieces_badly.draw( self.canvas, self.board, self.__move_start_square, False )

    def wait_for_human( self ):
        self.human_moved.clear()
        while not self.human_moved.is_set():
            self.human_moved.wait( 0.1 )
        return self.humans_move