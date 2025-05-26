from .position import Direction
from .pion import Pion
from .othellier import Othellier

class Coup:
    
    def __init__(self, pion : Pion, direction : Direction):
        self.pion_a_jouer = pion
        self.direction = direction
        self.pions_a_retourner = []
        self.coup_valide = False
        self.calcul_coup()
    
    def get_pion_a_jouer(self):
        return self.pion_a_jouer
    
    def add_pions_a_retourner(self, pion : Pion):
        self.pions_a_retourner.append(pion)
        
    def get_pions_a_retourner(self):
        return self.pions_a_retourner
        
    def get_coup_valide(self):
        return self.coup_valide
    
    def calcul_coup(self):
        fini = False
        pion_n_plus_un = self.pion_a_jouer.get_voisin(self.direction)
        
        while not fini:
            if pion_n_plus_un is not None :
                if pion_n_plus_un.get_couleur() != self.pion_a_jouer.get_couleur(): 
                    self.add_pions_a_retourner(pion_n_plus_un)
                if pion_n_plus_un.get_couleur() == self.pion_a_jouer.get_couleur():
                    self.coup_valide = True
                    fini = True
                    break
                pion_n_plus_un = pion_n_plus_un.get_voisin(self.direction)
            else:
                fini = True
                break
        
                