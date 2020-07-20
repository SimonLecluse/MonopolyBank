

class Model:

    def __init__(self):
        self.jackpot = 0
        self.nb_turn = 0
        self.pay = 0        # Montant de l'échange

    # modifier montant de la banque d'un joueur
    def add(self):
        pass

    def add_turn(self):
        self.nb_turn += 1


class Joueur:

    def __init__(self):
        self.bank = 0       #
        self.num = 0        # definit l'ordre de jeu
