from modele import Othellier, Joueur


class Vue :
    
    @staticmethod
    def afficher_plateau(othellier : Othellier):
        print(othellier)
         
    @staticmethod
    def demander_coup(joueur : Joueur):
        return input(f"{joueur}, entrez votre coup :")
     
    @staticmethod
    def demander_nom(numero : str):
        return input(f"Joueur {numero}, entrez votre nom :")

    @staticmethod
    def afficher_erreur(message: str):
        print(f"Erreur : {message}")
    
    @staticmethod
    def afficher_message(message: str):
        print(message)