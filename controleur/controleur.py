from modele import Partie
from vue.vue import Vue

class Controleur:
    
    def __init__(self):
        self.partie = None
        self.vue = Vue()
    
    def initPartie(self):
        nom_joueur_un = self.vue.demander_nom(numero="1")
        nom_joueur_deux = self.vue.demander_nom(numero="2")
        self.partie = Partie(nom_joueur_un, nom_joueur_deux)
        
    
    def boucle_jeu(self):
        """Boucle principale du jeu Othello."""
        self.vue.afficher_message("Bienvenue dans le jeu Othello !")
        
        #Initialisation de la partie
        self.initPartie()
        
        while not self.partie.get_est_terminee():
            joueur_courant = self.partie.get_joueur_courant()
            coups_possibles = self.partie.coupsPossibles(joueur_courant.get_couleur())
            
            if not coups_possibles:
                self.vue.afficher_message(f"Aucun coup possible pour {joueur_courant.get_nom()}. Tour passé.")
                self.partie.passer_tour()
                self.partie.update_est_terminee()
                continue  # passe au joueur suivant

            saisieIncorrecte = True
            while saisieIncorrecte:
                try:
                    saisieIncorrecte = False
                    self.vue.afficher_plateau(self.partie.get_othellier())
                    pos = self.vue.demander_coup(joueur_courant)
                    coup = self.partie.joue_coup(pos, joueur_courant, coups_possibles)

                    if coup:
                        self.vue.afficher_message(f"Coup joué par {joueur_courant.get_nom()} à la position {pos}.")
                    else:
                        self.vue.afficher_erreur("Ce coup n'est pas valide.")
                        saisieIncorrecte = True

                except ValueError as e:
                    self.vue.afficher_erreur(str(e))
                    saisieIncorrecte = True
            
            self.partie.passer_tour()
            self.partie.update_est_terminee()

        self.vue.afficher_plateau(self.partie.get_othellier())
        self.vue.afficher_message("La partie est terminée !")
        self.partie.update_gagnant()
        if self.partie.get_gagnant() is None:
            self.vue.afficher_message("Match nul !")
        else:
            self.vue.afficher_message(f"Le gagnant est {self.partie.get_gagnant().get_nom()}")     
        