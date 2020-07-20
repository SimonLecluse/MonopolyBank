from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout


class ViewMainFrame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("MonopolyBank")
        self.central_widget = ViewMainWidget()
        self.setCentralWidget(self.central_widget)


class ViewMainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.nb_players = 0
        self.players = [Player(), Player()]       # Contient tous les widgets joueurs dans une liste
        self.mod = '+'

        self.btn_mod = Buttons(self.mod, (20, 20), self.btn)
        self.btn_add_player = Buttons("Add Player", (80, 40), self.btn)
        self.btn_add_turn = Buttons("Turn Counter", (80, 40), self.btn)

        self.sig_add_player = None

        self.set_layouts()

    def set_layouts(self):

        layout_menu = QHBoxLayout()
        layout_menu.addWidget(self.btn_add_player)
        layout_menu.addWidget(self.btn_add_turn)
        layout_menu.addWidget(self.btn_mod)

        layout_players = QHBoxLayout()
        for p in self.players:
            layout_players.addWidget(p)

        layout_display = QVBoxLayout()
        layout_display.addLayout(layout_menu)
        layout_display.addLayout(layout_players)

        self.setLayout(layout_display)

    def btn(self):
        self.sig_add_player.emit()


class Buttons(QPushButton):

    def __init__(self, name, dim, callback, pos = (0,0)):
        QPushButton.__init__(self, str(name))

        self.setFixedWidth(dim[0])
        self.setFixedHeight(dim[1])

        self.pos = pos
        self.name = name

        # self.clicked.connect(lambda: callback(name))
        self.clicked.connect(callback)


class Player(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.btn_names = [1, 5, 10, 20, 50, 100, 500, "clear"]
        self.btn_players = []
        self.bank = 0
        self.bank_add = 0
        for i in range(len(self.btn_names)):
            self.btn_players.append(Buttons(str(self.btn_names[i]), (40, 20), ViewMainWidget.btn, (i//2, i%2) ))

        self.__set_layout()

    def __set_layout(self):

        self.layout_player_grid = QGridLayout()
        for b in self.btn_players:
            self.layout_player_grid.addWidget(b, b.pos[0], b.pos[1])

        self.setLayout(self.layout_player_grid)






