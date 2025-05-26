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
        self.initPartie()
            
        while not self.partie.get_est_terminee():
            saisieIncorrecte = True
            while saisieIncorrecte:
                try:
                    saisieIncorrecte = False
                    self.vue.afficher_plateau(self.partie.get_othellier())
                    joueur_courant = self.partie.get_joueur_courant()
                    pos = self.vue.demander_coup(joueur_courant)
                    coup = self.partie.joue_coup(pos, joueur_courant)
                    if coup:
                        self.vue.afficher_message(f"Coup joué par {joueur_courant.get_nom()} à la position {pos}.")
                    else:
                        self.vue.afficher_message("Aucun coup n'est possible pour le joueur courant !")
                except ValueError as e:
                    self.vue.afficher_erreur(str(e))
                    saisieIncorrecte = True
                    

        self.vue.afficher_plateau(self.partie.get_othellier())
        self.vue.afficher_message("La partie est terminée !")
        self.vue.afficher_message(f"Le gagnant est {self.partie.get_gagnant().get_nom()}")        
    