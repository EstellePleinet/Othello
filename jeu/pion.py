from enum import Enum
from .position import Direction

class Couleur(Enum):
    BLANC = 'b'
    NOIR = 'n'

class Pion:
    def __init__(self, couleur):
        self.couleur = couleur
        self.voisins = {d: None for d in Direction} 
        self.pos = None

    def get_couleur(self):
        return self.couleur

    def get_couleur_opposee(self):
        if (self.couleur == Couleur.BLANC):
            return Couleur.NOIR
        return Couleur.BLANC
    
    def retourne(self):
        self.couleur = self.couleur.opposée()

    def set_position(self, pos):
        self.pos = pos

    def get_position(self):
        return self.pos
    
    def is_voisin_complet(self):
        return all(self.voisins is not  None for voisin in self.voisins.values)
    
    def directions_voisin_possible(self):
        [direction for direction, voisin in self.voisins.items() if voisin is None]
        

    def __str__(self):
        return f"{self.couleur.value}"
    