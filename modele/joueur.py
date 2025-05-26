from .pion import Couleur

class Joueur:
    
    def __init__(self, nom, couleur: Couleur):
        if not isinstance(couleur, Couleur):
            raise ValueError("La couleur doit être une instance de Couleur")
        self.nom = nom
        self.couleur = couleur
        
    def get_nom(self) : return self.nom
    
    def get_couleur(self) : return self.couleur
        
    def __str__(self):
        return f"{self.nom} jouant les pions {self.couleur}"