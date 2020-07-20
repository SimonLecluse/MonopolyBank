from src.model import Model
from src.view.view import ViewMainFrame, Player
from PySide2.QtCore import QObject, Signal, Slot


class Controller(QObject):

    sig_add_player = Signal()
    btn_bank_signal = Signal(str)

    def __init__(self):
        QObject.__init__(self)

        self.gui = ViewMainFrame()
        self.gui.show()

        # Connexion des signaux aux fonctions correspondantes
        self.sig_add_player.connect(self.add_player)
        self.gui.central_widget.sig_add_player = self.sig_add_player


    @Slot()
    def add_player(self):
        self.gui.central_widget.players.append(Player())
        self.gui.central_widget.set_layouts()
        print(self.gui.central_widget.players)


