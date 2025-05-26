import re
import string
from .pion import Pion, Couleur
from .position import Position, Direction

class Othellier :
    
    def __init__(self, taille=8):
        self.taille = taille
        self._grille = [[None for colonne in range(taille)] for ligne in range(taille)]
        self.__init_grille()
    
    @staticmethod
    def est_position_valide_str(entree: str, taille=8) -> bool:
        return bool(re.match(f"^[A-Ha-h][1-{taille}]$", entree.strip()))
    
    def est_rempli(self):
        return all(all(casee is not None for casee in ligne ) for ligne in self._grille)
    
    def get_grille(self):
        return self._grille
    
    def case_exist(self, pos: Position):
        x, y = pos.get_x(), pos.get_y()
        return 0 <= x < self.taille and 0 <= y < self.taille
    
    def get_case(self, pos: str):
        position = Position(label=pos)
        return self._grille[position.get_x()][position.get_y()]
    
    def _get_case(self, pos : Position):
        return self._grille[pos.get_x()][pos.get_y()]
         
    def set_case(self, pion : Pion):
        position = pion.get_position()
        if self._grille[position.get_x()][position.get_y()] is None:
            self._grille[position.get_x()][position.get_y()] = pion
        else : 
            raise ValueError("Case déjà occupée")
        
    def mettre_a_jour_voisins_autour(self, pion: Pion):
        position = pion.get_position()
        pion_central = self._get_case(position)

        if pion_central is None:
            return  # Rien à faire si aucun pion sur cette case

        for direction in Direction:
            pos_voisine = position.prochaine_pos_dans_direction(direction)

            # Vérifie que la position est bien dans le plateau
            if self.case_exist(pos_voisine):
                pion_voisin = self._get_case(pos_voisine)

                # Mise à jour du voisin dans la direction
                pion_central.ajoute_voisin(direction, pion_voisin)

                # Mise à jour réciproque du voisin (si un pion existe)
                if pion_voisin is not None:
                    direction_opposee = Direction.get_direction_opposee(direction)
                    pion_voisin.ajoute_voisin(direction_opposee, pion_central)
            else:
                # Hors plateau → pas de voisin
                pion_central.ajoute_voisin(direction, None)
        
    def __init_grille(self):
        """Initialise la grille avec les pions de départ."""
        dquatre = Pion(Couleur.NOIR, Position(label="D4"))
        equatre = Pion(Couleur.BLANC, Position(label="E4"))
        dcinquante = Pion(Couleur.BLANC, Position(label="D5"))
        ecinq = Pion(Couleur.NOIR, Position(label="E5"))
        
        self.set_case(dquatre)
        self.set_case(equatre)
        self.set_case(dcinquante)
        self.set_case(ecinq)
    
        self.mettre_a_jour_voisins_autour(dquatre)
        self.mettre_a_jour_voisins_autour(equatre)
        self.mettre_a_jour_voisins_autour(dcinquante)
        self.mettre_a_jour_voisins_autour(ecinq)
        
        
    def __str__(self):
        colonnes = list(string.ascii_uppercase[:self.taille])  # ['A', 'B', ..., 'H']
        
        grille_str = "  " + " ".join(colonnes) + "\n"
        for i, ligne in enumerate(self._grille):
            grille_str += str(i + 1) + " "
            for case in ligne:
                if case is None:
                    grille_str += ". "
                else:
                    grille_str += str(case) + " "
            grille_str += "\n"
        return grille_str
    
    