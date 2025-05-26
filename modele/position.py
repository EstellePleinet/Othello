from enum import Enum
import re

class Direction(Enum):
    NORD = (-1, 0)
    SUD = (1, 0)
    EST = (0, 1)
    OUEST = (0, -1)
    NORD_EST = (-1, 1)
    NORD_OUEST = (-1, -1)
    SUD_EST = (1, 1)
    SUD_OUEST = (1, -1)
    
    def get_direction_opposee(self):
        opposee = (-self.value[0], -self.value[1])
        for direction in Direction :
            if direction.value == opposee:
                return direction
    
class Position:
    
    def __init__(self, ligne=None, colonne=None, label=None):
        if label:
            self._label = label
            self._x = None
            self._y = None
            self.to_position()
        elif ligne is not None and colonne is not None:
            self._x = ligne
            self._y = colonne
            self._label = ""
            self.to_string()
        else:
            raise ValueError("Il faut fournir soit un label, soit une paire (ligne, colonne).")
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_label(self):
        return self._label
    
    def prochaine_pos_dans_direction(self, direction: Direction) :
        dx, dy = direction.value
        return Position(self._x + dx, self._y + dy)
    
    def to_position(self) -> bool :
        colonnes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        col_letter = self.get_label()[0].upper()
        self._y = colonnes.index(col_letter)
        self._x = int(self.get_label()[1]) - 1

    def to_string(self) :
        colonnes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lettre = str(colonnes[self.get_y()])
        nombre = str(self.get_x() + 1)
        self._label = lettre + nombre        
    
    def __eq__(self, other):
        if isinstance(other, Position):
            return self._x == other._x and self._y == other._y
        return False