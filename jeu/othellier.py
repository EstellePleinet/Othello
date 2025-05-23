import re
import string
from .pion import Pion, Couleur

class Othellier :
    
    def __init__(self):
        taille = 8
        self._grille = [[None for colonne in range(taille)] for ligne in range(taille)]
        self._colonnes = list(string.ascii_uppercase[:taille])  # ['A', 'B', ..., 'H']
        self._lignes = list(range(1, taille + 1))  # [1, 2, ..., 8]
        self.__init_grille()
        
    @staticmethod
    def __est_position_valide(entree: str, taille=8) -> bool:
        return bool(re.match(f"^[A-Ha-h][1-{taille}]$", entree.strip()))
   
    def __est_vide(self, pos):
        lig, col = self.__convertir_position(pos)
        return self._grille[lig][col] is None
    
    def __convertir_position(self, pos: str):
        if self.__est_position_valide(pos):
            col_letter = pos[0].upper()
            lig = int(pos[1]) - 1
            col = self._colonnes.index(col_letter)
            return lig, col
        else:
            raise ValueError("Position invalide")

    def get_case(self, pos: str):
        lig, col = self.__convertir_position(pos)
        return self._grille[lig][col]
    
    def _get_case(self, lig: int, col: int):
        return self._grille[lig][col]
         
    def __set_case(self, pos: str, pion):
        lig, col = self.__convertir_position(pos)
        if self._grille[lig][col] is None:
            self._grille[lig][col] = pion
        else : 
            raise ValueError("Case déjà occupée")
        
    def __init_grille(self):
        self.__set_case("D4", Pion(Couleur.NOIR))
        self.__set_case("E5", Pion(Couleur.NOIR))
        self.__set_case("D5", Pion(Couleur.BLANC))
        self.__set_case("E4", Pion(Couleur.BLANC))
    
    def __coups_possibles(self, couleur):
       for ligne in range(8):
            for colonne in range(8):
                if self._grille[ligne][colonne] is None:
                    # Vérifier si le coup est valide
                    if self.__est_coup_valide(ligne, colonne, couleur):
                        return True
    
    def __coup_valide(pos, couleur):
        # nord, sud, est, ouest, nord-est, nord-ouest, sud-est, sud-ouest
        directions = [(-1,0), (1,0), (0,1), (0,-1), (-1,1), (-1,-1), (1,1), (1,-1)]
        # nord, sud
        return
    
    def joue_coup(self, pos: str, pion: Pion):
        lig, col = self.__convertir_position(pos)
        try : 
            self.__set_case(pos, pion)
        except ValueError as e:
            print(e)
            return False

        
    def __str__(self):
        grille_str = "  " + " ".join(self._colonnes) + "\n"
        for i, ligne in enumerate(self._grille):
            grille_str += str(i + 1) + " "
            for case in ligne:
                if case is None:
                    grille_str += ". "
                else:
                    grille_str += str(case) + " "
            grille_str += "\n"
        return grille_str
    
    