class Coup:
    
    def __init__(self, pion):
        self.pion_a_jouer = pion
        self.pions_a_retourner = []
    
    def get_pion_a_jouer(self):
        return self.pion_a_jouer
    
    def add_pion_a_retourner(self, pion):
        self.pions_a_retourner.append(pion)