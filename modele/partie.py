from .joueur import Joueur
from .pion import Pion, Couleur
from .position import Position, Direction
from .othellier import Othellier
from .coup import Coup

class Partie:
    
    def __init__(self, joueur_un : str, joueur_deux : str, taille = 8):
        self.othellier = Othellier(taille)
        self.est_terminee = False
        self.joueurs = [Joueur(joueur_un, Couleur.NOIR), Joueur(joueur_deux, Couleur.BLANC)]
        self.joueur_courant = False #Faux = 0, J1, Vrai = 1, J2
        self.gagnant = None
        
    def get_gagnant(self):
        if self.gagnant is None:
            raise ValueError("Aucun gagnant")
        return self.gagnant
        
    def get_othellier(self): return self.othellier
    
    def get_joueur_courant(self): return self.joueurs[int(self.joueur_courant)]
    
    def get_est_terminee(self):
        return self.est_terminee
    
    def check_est_terminee(self):
        coups_possibles_noirs = self._coupsPossibles(Couleur.NOIR)
        coups_possibles_blancs = self._coupsPossibles(Couleur.BLANC)
        
        self.est_terminee = not (coups_possibles_noirs or coups_possibles_blancs)
        
        if (self.est_terminee):
            # On détermine le gagnant
            pions_noirs = self._get_all_pions_of_color(Couleur.NOIR)
            pions_blancs = self._get_all_pions_of_color(Couleur.BLANC)
            if len(pions_noirs) > len(pions_blancs):
                self.gagnant = self.joueurs[0]
        
    def _get_all_pions_of_color(self, couleur : Couleur):
        pions = []
        for i, ligne in enumerate(self.othellier.get_grille()):        # i : index de ligne, ligne : liste de cases    
            for j, pion in enumerate(ligne):            # j : index de colonne, case : contenu (Pion ou None)
                if pion is not None :
                    if pion.get_couleur() == couleur :
                        pions.append(pion)
        return pions
    
    def _coupsPossibles(self, couleur : Couleur):
        """Calculs les coups possibles pour une couleur donnée."""
        coups_possibles = []
        # Liste des pions de couleur opposée à côté desquels il est possible de jouer :
        pions = self._get_all_pions_of_color(couleur.opposee())
        
        #Calculs des coups possibles :
        for pion in pions :
            # Pour chaque Pion on récupère les emplacements voisins possibles
            directions = pion.directions_voisin_possible()
            # Si tout les voisins sont pris : le coup n'est pas jouable 
            if directions :
                # On calcule l'emplacement correspondant à la direction
                for direction in directions :
                    position_pion_a_jouer = pion.get_position().prochaine_pos_dans_direction(direction)
                    # Si la place existe sur le plateau alors
                    if (self.othellier.case_exist(position_pion_a_jouer)):
                        pion_actuel = Pion(couleur, position_pion_a_jouer)
                        #on set temporairement la voisin du pion actuel
                        pion_actuel.ajoute_voisin(direction.get_direction_opposee(), pion)
                        coup = Coup(pion_actuel, direction.get_direction_opposee())
                        if coup.get_coup_valide():
                            coups_possibles.append(coup)
            
        return coups_possibles
    
    def _coupCompatibles(self, coups_possibles, pion):
        """Filtre les coups possibles pour ne garder que ceux qui sont compatibles avec le pion donné"""
        coups_compatibles = []
        for coup_possible in coups_possibles:
            if coup_possible.get_pion_a_jouer().get_position() == pion.get_position():
                coups_compatibles.append(coup_possible)
        return coups_compatibles
    
    def _retourne_pions(self, coups_compatibles, pion, joueur):
        """Retourne les pions selon les coups compatibles"""
        for coup_compatible in coups_compatibles:
            for pion_a_retourner in coup_compatible.get_pions_a_retourner():
                position_pion = pion_a_retourner.get_position()
                self.othellier._get_case(position_pion).retourne()
    
    def _update_voisins(self, pion):
        # Met à jour les voisins du pion joué
        self.othellier.mettre_a_jour_voisins_autour(pion)
        for voisin in pion.get_voisins().values():
            if voisin is not None:
                self.othellier.mettre_a_jour_voisins_autour(voisin)
    
    def joue_coup(self, pos: str, joueur : Joueur):
        pos = pos.upper().strip()
        if (self.othellier.est_position_valide_str(pos)):
            position = Position(label=pos)
            pion = Pion(joueur.get_couleur(), position)
            coups_possibles = self._coupsPossibles(pion.get_couleur())
            if not coups_possibles:
                return False
            coups_compatibles = self._coupCompatibles(coups_possibles, pion)
            if not coups_compatibles:
                raise ValueError("Aucun coup n'est possible à cette position.")
            
            self.othellier.set_case(pion)
            self._retourne_pions(coups_compatibles, pion, joueur)
            self._update_voisins(pion)
            # Met à jour l'état de la partie
            self.check_est_terminee()
            #Mise à jour du joueur actuel qui joue !
            self.joueur_courant = not self.joueur_courant
            return True
        else:
            raise ValueError("La position n'est pas valide. Veuillez rentrer une case type 'A2'")
        
            
         
    

        