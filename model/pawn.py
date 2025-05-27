from enum import Enum
from .position import Direction, Position

class Color(Enum):
    BLACK = '◯'
    WHITE = '◉'
    
    def opposite(self):
        return Color.BLACK if self == Color.WHITE else Color.WHITE
    
    def __str__(self):
        return self.value

class Pawn:
    def __init__(self, color: Color):
        self._color = color 

    @property
    def color(self):
        return self._color

    def flip(self):
        self._color = self.color.opposite()
        
    def __str__(self):
        return str(self.color)

   

    