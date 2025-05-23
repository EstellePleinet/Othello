from .pion import Pion, Couleur, Direction
from .othellier import Othellier
from .coup import Coup

class Partie:
    
    def __init__(self, othellier : Othellier):
        self.othellier = othellier
        
    def _get_all_pions_of_color(self, couleur : Couleur):
        pions = []
        for i, ligne in enumerate(self.othellier.get_grille()):        # i : index de ligne, ligne : liste de cases    
            for j, pion in enumerate(ligne):            # j : index de colonne, case : contenu (Pion ou None)
                if pion is not None :
                    if pion.get_couleur() == couleur :
                        pions.append(pion)
        return pions
    
    def _coupsPossibles(self, pion : Pion):
        coups_possibles = []
        #La listes des pions de couleurs opposés a côté desquels jouer possiblement :
        pions = self._get_all_pions_of_color(pion.get_couleur_opposee())
        #Calculs des coups possibles :
        for pion in pions :
            # Pour chaque Pion on récupère les emplacements voisins possibles
            directions = pion.directions_voisin_possible()
            # Si tout les voisins sont pris : le coup n'est pas jouable 
            if directions :
                # On calcule l'emplacement correspondant à la direction
                for direction in directions :
                    position_pion_a_jouer = pion.get_position.dans_direction(direction)
                    # Si la place existe sur le plateau alors
                    # On calcule les coups possibles
                    
        #Je récupère tout les coups possible valide qui commence par la position de mon pion et j'applique ! 
                    
                # Si le coup est valide alors on l'ajoute a coups possible 
                
            # Si il existe de la place alors on pose le pion et on commence à calculer le coup dans la direction donnée
            # On vérifie qu'on peut poser le pion dans la case dite.
            # La direction donnée : Si on pose le pion au sud alors le premier pion a retourner est l'actuel et on prend son nord. 
            # Si on rencontre notre couleur le coup est fini et valide
            # Si on ne rencontre jamais notre couleur le coup est invalide
            
        return coups_possibles
    
    def joue_coup(self, pion: Pion):
        
        #La liste des coups possibles
        
        #Est ce que pos est dans la liste des coups possibles ?
        
        #On joue le coup possible selectionné
        return None