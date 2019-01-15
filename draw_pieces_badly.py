from tkinter import *

class DrawPiecesBadly:
    def __init__(self):
        self.width = 400.0

    def draw(self,canvas):
        dark=False
        for x in range(0,8):
            dark = not dark
            for y in range(0,8):
                dark = not dark
                fill_color = '#707070' if dark else '#a0a0a0'
                canvas.create_rectangle( x*self.width/8, y*self.width/8, (x+1)*self.width/8, (y+1)*self.width/8, outline=fill_color, fill=fill_color )

