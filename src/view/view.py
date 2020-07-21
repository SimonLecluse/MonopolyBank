from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QRadioButton, QComboBox
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PySide2.QtGui import QPalette, QColor



class ViewMainFrame(QMainWindow):
    def __init__(self, list_players, start_money):
        QMainWindow.__init__(self)
        self.setWindowTitle("MonopolyBank")
        self.central_widget = ViewMainWidget(list_players, start_money)
        self.setCentralWidget(self.central_widget)


class ViewMainWidget(QWidget):

    def __init__(self, list_players, start_money):
        QWidget.__init__(self)

        self.nb_players = len(list_players)
        self.players = [Player(list_players[i], i+1, self, start_money) for i in range(self.nb_players)]       # list of widgets players
        self.__trade_value = 0

        # Widgets
        self.combo_trade1 = QComboBox()
        self.combo_trade1.addItems(list_players)
        self.combo_trade1.setFixedWidth(100)

        self.combo_trade2 = QComboBox()
        self.combo_trade2.addItems(list_players)
        self.combo_trade2.setFixedWidth(100)

        # select value of trade
        self.trade_value_label = QLabel()
        self.trade_value_label.setText("0")
        self.trade_value_name = QLabel()
        self.trade_value_name.setText("Valeur de l'échange:  ")

        self.btn_validate_trade = Buttons("Valider echange:", (120, 40), self.btn_trade_pressed)
        self.btn_trade_names = [1, 5, 10, 20, 50, 100, 500, "clear"]
        self.btn_trade = [Buttons(str(self.btn_trade_names[i]), (40, 20), self.btn_trade_pressed, (i // 2, i % 2)) for i in range(len(self.btn_trade_names))]

        # Signals
        self.sig_player_bank = None
        self.sig_trade = None


        self.__set_layouts()

    def __set_layouts(self):

        # Layout menu for trades between players
        layout_menu = QHBoxLayout()
        layout_menu.addWidget(self.btn_validate_trade)
        layout_menu.addWidget(self.combo_trade1)
        layout_menu.addWidget(self.combo_trade2)
        layout_menu.addWidget(self.trade_value_name)
        layout_menu.addWidget(self.trade_value_label)

        # Buttons values
        layout_menu_trade = QGridLayout()
        for b in self.btn_trade:
            layout_menu_trade.addWidget(b, b.pos[0], b.pos[1])

        layout_menu.addLayout(layout_menu_trade)

        # containing all players in a QHBoxLayout, bellow layout menu
        layout_players = QHBoxLayout()
        for p in self.players:
            layout_players.addWidget(p)

        layout_display = QVBoxLayout()
        layout_display.addLayout(layout_menu)
        layout_display.addLayout(layout_players)

        self.setLayout(layout_display)

    def btn_player_pressed(self, x):
        self.sig_player_bank.emit(x)

    def btn_trade_pressed(self, x):
        self.sig_trade.emit(x[0])

    def set_trade_value(self, value):
        self.__trade_value = value
        self.trade_value_label.setText(str(self.__trade_value))


class Buttons(QPushButton):

    def __init__(self, name, dim, callback, pos=(0, 0), player=[0, 0]):
        QPushButton.__init__(self, str(name))

        self.setFixedWidth(dim[0])
        self.setFixedHeight(dim[1])

        if name == "ok":
            self.setStyleSheet("background: #bbffbb;")
        elif name == "clear":
            self.setStyleSheet("background: #ffbbbb;")

        self.pos = pos
        self.name = str(name)
        self.infos = (name, player[1])

        self.clicked.connect(lambda: callback(self.infos))


class Player(QWidget):
    def __init__(self, player_name, player_nb, central_widget, start_money):
        QWidget.__init__(self)

        self.__bank = start_money
        self.__bank_add = 0
        self.player_name = player_name

        # Widgets

        # Boutons
        self.btn_names = [1, 5, 10, 20, 50, 100, 500, 1000, "clear", "ok"]
        self.btn_players = []
        for i in range(len(self.btn_names)):
            self.btn_players.append(Buttons(self.btn_names[i], (40, 20), central_widget.btn_player_pressed, (i//2 + 2, i%2), [player_name, player_nb - 1]))

        self.mod_plus = QRadioButton('+')
        self.mod_plus.setChecked(True)
        self.mod_sub = QRadioButton('-')

        # Labels
        self.player_name_label = QLabel()
        self.player_name_label.setText(str(player_nb) + ": " + player_name)

        self.bank_label = QLabel()
        self.bank_label.setText(str(self.__bank))
        self.bank_name_label = QLabel()
        self.bank_name_label.setText("Banque:")

        self.bank_add_label = QLabel()
        self.bank_add_label.setText(str(self.__bank_add))
        self.bank_add_name_label = QLabel()
        self.bank_add_name_label.setText("Virement:")

        self.__set_layout()

        self.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor("#dddddd" if player_nb % 2 == 0 else "#ddddff"))
        self.setPalette(pal)

    def __set_layout(self):

        self.layout_player = QGridLayout()
        self.layout_bank = QHBoxLayout()

        # Buttons
        for b in self.btn_players:
            self.layout_player.addWidget(b, b.pos[0], b.pos[1])
        self.layout_player.addWidget(self.mod_sub,8,0)
        self.layout_player.addWidget(self.mod_plus,8,1)

        # Labels
        self.layout_player.addWidget(self.bank_label, 1,1)
        self.layout_player.addWidget(self.bank_name_label, 1,0)
        self.layout_player.addWidget(self.bank_add_label, 7, 1)
        self.layout_player.addWidget(self.bank_add_name_label, 7, 0)
        self.layout_player.addWidget(self.player_name_label,0,0)

        self.setLayout(self.layout_player)

    def set_bank_add(self, val):
        """Setter for __bank_add"""
        self.__bank_add = val
        self.bank_add_label.setText(str(self.__bank_add))

    def get_bank_add(self):
        """Getter for __bank_add"""
        return self.__bank_add

    def set_bank(self, val):
        """Setter for __bank"""
        self.__bank = val
        self.bank_label.setText(str(self.__bank))

    def get_bank(self):
        """Getter for __bank"""
        return self.__bank







