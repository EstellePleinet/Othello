from enum import Enum

class Couleur(Enum):
    BLANC = 'b'
    NOIR = 'n'

class Pion:
    def __init__(self, couleur):
        self.couleur = couleur
        self.ligne = None
        self.colonne = None

    def get_couleur(self):
        return self.couleur
    
    def get_ligne(self):
        return self.ligne
    
    def get_colonne(self):
        return self.colonne
    
    def set_ligne(self, ligne):
        self.ligne = ligne
        
    def set_colonne(self, colonne):
        self.colonne = colonne
    
    def get_opposite(self):
        if self.couleur == Couleur.BLANC:
            return Couleur.NOIR
        else:
            return Couleur.BLANC
        
    def retourne_pion(self):
        self.couleur = self.get_opposite()
    
    def __str__(self):
        return f"{self.couleur.value}"
    