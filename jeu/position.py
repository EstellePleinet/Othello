from enum import Enum

class Direction(Enum):
    NORD = (-1, 0)
    SUD = (1, 0)
    OUEST = (0, -1)
    EST = (0, 1)
    NORD_OUEST = (-1, -1)
    NORD_EST = (-1, 1)
    SUD_OUEST = (1, -1)
    SUD_EST = (1, 1)
    
class Position:
    
    def __init__(self, ligne, colonne):
        self._x = ligne
        self._y = colonne
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def dans_direction(self, direction: Direction):
        dx, dy = direction.value
        return Position(self._x + dx, self._y + dy)