from enum import Enum
from .position import Direction, Position

class Couleur(Enum):
    NOIR = '◯'
    BLANC = '◉'
    
    def opposee(self):
        if self == Couleur.BLANC:
            return Couleur.NOIR
        return Couleur.BLANC
    
    def __str__(self):
        return self.value
        

class Pion:
    def __init__(self, couleur : Couleur, position : Position):
        self.couleur = couleur
        self.voisins = {d: None for d in Direction} 
        self.pos = position

    def get_couleur(self):
        return self.couleur

    def get_voisin(self, direction : Direction):
        return self.voisins[direction]
    
    def get_voisins(self):
        return self.voisins
    
    def ajoute_voisin(self, direction : Direction, pion_voisin : 'Pion'):
        if direction in self.voisins:
            self.voisins[direction] = pion_voisin
        else:
            raise ValueError("Direction invalide pour ajouter un voisin.")
    
    def retourne(self):
        self.couleur = self.couleur.opposee()

    def set_position(self, pos : Position):
        self.pos = pos

    def get_position(self):
        return self.pos
    
    def is_voisin_complet(self):
        return all(self.voisins is not  None for voisin in self.voisins.values)
    
    def directions_voisin_possible(self):
        return [direction for direction, voisin in self.voisins.items() if voisin is None]

    def __str__(self):
        return f"{self.couleur.value}"
    