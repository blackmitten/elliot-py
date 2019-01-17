from collections import namedtuple

Vector = namedtuple('Vector', ['x', 'y'])

class Square(namedtuple('Square', ['x', 'y'])):

    def in_bounds(self):
        return self.x >= 1 and self.x <= 8 and self.y >= 1 and self.y <= 8

    @staticmethod
    def from_notation( s ):
        x = ord(s[0]) - 96
        y = ord(s[1]) - 48

        square = Square(x, y)
        if( not square.in_bounds() ):
            raise RuntimeError("Square out of bounds")
        
        return square

    def __sub__(self, other):
        return Vector( self.x - other.x, self.y - other.y )

    def offset(self, dx, dy):
        return Square( self.x + dx, self.y + dy)

    def __str__(self):
        if self.x < 1 or self.x > 8 or self.y < 1 or self.y > 8:
            return "Invalid"
        s = chr(self.x + 96) + chr(self.y + 48)
        return s