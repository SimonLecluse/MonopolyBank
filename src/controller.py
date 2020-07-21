from src.model import Model
from src.view.view import ViewMainFrame
from PySide2.QtCore import QObject, Signal, Slot

class Controller(QObject):

    sig_bank_player = Signal(tuple)
    sig_trade = Signal(str)

    def __init__(self, list_players, start_money):
        QObject.__init__(self)

        self.gui = ViewMainFrame(list_players, start_money)
        self.gui.show()
        self.m = Model(list_players, start_money)

        # Signals
        self.gui.central_widget.sig_player_bank = self.sig_bank_player
        self.sig_bank_player.connect(self.player_bank)

        self.gui.central_widget.sig_trade = self.sig_trade
        self.sig_trade.connect(self.player_trade)

        self.list_players = list_players

    @Slot(tuple)
    def player_bank(self, x):
        # x = [value, nb_player]
        if type(x[0]) is int:
            self.m.set_bank_add(x[1], x[0] + self.m.get_players()[x[1]][1])
            self.gui.central_widget.players[x[1]].set_bank_add(self.m.get_players()[x[1]][1])
        else:
            if x[0] == "clear":
                self.m.set_bank_add(x[1],0)
                self.gui.central_widget.players[x[1]].set_bank_add(self.m.get_players()[x[1]][1])
            elif x[0] == "ok":
                # bank player +/- = bank_add player
                self.m.set_bank(x[1], self.gui.central_widget.players[x[1]].mod_plus.isChecked())
                self.gui.central_widget.players[x[1]].set_bank(self.m.get_players()[x[1]][0])
                self.gui.central_widget.players[x[1]].set_bank_add(self.m.get_players()[x[1]][1])

    @Slot(str)
    def player_trade(self, btn_value):
        if btn_value in ["1", "5", "10", "20", "50", "100", "500", "1000"]:
            self.m.trade_value += int(btn_value)
            self.gui.central_widget.set_trade_value(self.m.trade_value)
        else:
            if btn_value == "clear":
                self.m.trade_value = 0
                self.gui.central_widget.set_trade_value(self.m.trade_value)

            elif btn_value == "Valider echange:":
                p1 = self.gui.central_widget.combo_trade1.currentText()
                p2 = self.gui.central_widget.combo_trade2.currentText()
                p1_nb, p2_nb = self.list_players.index(p1), self.list_players.index(p2)
                self.m.trade(p1_nb, p2_nb)
                self.gui.central_widget.players[p1_nb].set_bank(self.m.get_players()[p1_nb][0])
                self.gui.central_widget.players[p2_nb].set_bank(self.m.get_players()[p2_nb][0])
                self.gui.central_widget.set_trade_value(0)


