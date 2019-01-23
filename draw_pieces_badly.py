#from tkinter import canvas
from backend.pieces import PieceVisitor

class DrawPiecesBadly(PieceVisitor):
    def __init__(self):
        self.width = 400.0
        self.square_width = self.width / 8

    def draw( self, canvas, board, start_square, machine_thinking ):
        dark=False
        for x in range(0,8):
            dark = not dark
            for y in range(0,8):
                dark = not dark
                fill_color = '#707070' if dark else '#a0a0a0'
                canvas.create_rectangle( x*self.square_width, y*self.square_width, 
                    (x+1)*self.square_width, (y+1)*self.square_width, outline=fill_color, fill=fill_color )
        if board is not None:
            for piece in board.black_pieces:
                piece.accept( self, canvas )
            for piece in board.white_pieces:
                piece.accept( self, canvas )
        if start_square.in_bounds():
            canvas.create_rectangle( (start_square.x - 1) * self.square_width, (8 - start_square.y) * self.square_width,
                (start_square.x) * self.square_width, (9 - start_square.y) * self.square_width, outline = 'red', width = 4 )
    
    def draw_piece_preamble( self, piece ):
        color = 'white' if piece.white else 'black'
        x = piece.pos.x * self.square_width - self.square_width / 2
        y = (9 - piece.pos.y) * self.square_width - self.square_width / 2
        return x, y, color

    def visit_pawn(self, pawn, canvas):
        x, y, color = self.draw_piece_preamble( pawn )
        canvas.create_oval( x - self.square_width / 5, y - self.square_width / 5,
            x + self.square_width / 5, y + self.square_width / 5, outline=color, fill=color )

    def visit_king(self, king, canvas):
        x, y, color = self.draw_piece_preamble( king )
        canvas.create_rectangle( x - self.square_width / 7, y - self.square_width / 3.5,
            x + self.square_width / 7, y + self.square_width / 3.5, outline=color, fill=color )
        canvas.create_rectangle( x - self.square_width / 3.5, y - self.square_width / 7,
            x + self.square_width / 3.5, y + self.square_width / 7, outline=color, fill=color )

    def visit_rook(self, rook, canvas):
        x, y, color = self.draw_piece_preamble( rook )
        canvas.create_rectangle( x - self.square_width / 7, y - self.square_width / 4, 
            x + self.square_width / 7, y + self.square_width / 4, outline=color, fill=color )
        canvas.create_rectangle( x - self.square_width / 5, y - self.square_width/4, 
            x + self.square_width / 5, y - self.square_width / 8, outline =color, fill=color )
        canvas.create_rectangle( x - self.square_width / 5, y + self.square_width/4, 
            x + self.square_width / 5, y + self.square_width / 8, outline =color, fill=color )

    def visit_queen(self, queen, canvas):
        x, y, color = self.draw_piece_preamble( queen )
        canvas.create_polygon([x-self.square_width/3.5, y+self.square_width/7,
            x+self.square_width/3.5, y + self.square_width/7,
            x, y - self.square_width / 3 ], outline=color, fill=color )
        canvas.create_polygon([ x - self.square_width / 3.5, y - self.square_width / 7,
            x + self.square_width / 3.5, y - self.square_width / 7,
            x, y + self.square_width / 3 ], outline=color, fill=color )

    def visit_bishop(self, bishop, canvas):
        x, y, color = self.draw_piece_preamble( bishop )
        canvas.create_polygon( [ x - self.square_width / 5, y + self.square_width / 4,
            x + self.square_width / 5, y + self.square_width / 4,
            x, y - self.square_width / 4 ], outline=color, fill=color )

    def visit_knight(self, knight, canvas):
        x, y, color = self.draw_piece_preamble( knight )
        canvas.create_rectangle( x - self.square_width / 5, y - self. square_width / 4,
            x + 3 * self.square_width / 35, y + self.square_width / 4, outline=color, fill=color )
        canvas.create_rectangle( x - self.square_width / 5, y - self. square_width / 4,
            x + self.square_width / 5, y, outline=color, fill=color )
