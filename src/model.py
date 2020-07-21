
class Model:

    def __init__(self, list_players, start_money):

        # Caractéristiques des joueurs [bank, bank_add]
        self.__players = [[start_money, 0] for _ in range(len(list_players))]

        self.trade_value = 0

    # modifier montant de la banque d'un joueur

    def set_bank_add(self, player_nb, value):
        """add value to player's add_bank"""
        self.__players[player_nb][1] = value

    def get_players(self):
        return self.__players

    def set_bank(self, player_nb, mod_plus):
        """add/sub bank_add to bank"""
        if mod_plus:
            self.__players[player_nb][0] += self.__players[player_nb][1]
        else:
            self.__players[player_nb][0] -= self.__players[player_nb][1]
        self.__players[player_nb][1] = 0

    def trade(self, player_nb1, player_nb2):
        self.__players[player_nb1][0] -= self.trade_value
        self.__players[player_nb2][0] += self.trade_value

