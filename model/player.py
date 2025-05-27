from .pawn import Color

class Player:
    
    def __init__(self, name, color: Color, is_human : bool = True):
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of Couleur")
        self._name = name
        self._color = color
        self._is_human = is_human
        
    @property   
    def name(self): 
        return self._name
    
    @property
    def color(self): 
        return self._color
    
    @property
    def is_human(self):
        return self._is_human
        
    def __str__(self):
        return f"{self.name} playing {self.color} pieces"
