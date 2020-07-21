from PySide2.QtWidgets import QDialog, QComboBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout


class CustomDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Paramétrage")

        # Widgets
        self.combo_players = QComboBox()
        self.combo_players.addItems([str(i) for i in range(2, 11)])
        self.combo_players.setFixedWidth(100)
        self.combo_players.activated.connect(self.__on_nb_players_changed)

        self.btn_validate = QPushButton("Valider")
        self.btn_validate.clicked.connect(self.accept)

        self.line_edits = []
        self.player_name = []
        for _ in range(9):
            self.line_edits.append(QLineEdit())
            self.line_edits[-1].setVisible(False)

        # solde de départ
        self.start_money_name = QLabel()
        self.start_money_name.setText("Argent de départ")
        self.start_money = QLineEdit()



        # Layouts
        self.layout_param = QVBoxLayout()
        self.layout_param.addWidget(self.combo_players)
        for i in self.line_edits:
            self.layout_param.addWidget(i)

        self.layout_start_money = QHBoxLayout()
        self.layout_start_money.addWidget(self.start_money_name)
        self.layout_start_money.addWidget(self.start_money)

        self.layout_param.addLayout(self.layout_start_money)
        self.layout_param.addWidget(self.btn_validate)

        self.setLayout(self.layout_param)

        self.__on_nb_players_changed()


    def __on_nb_players_changed(self):
        for i in range(len(self.line_edits)):
            self.line_edits[i].setVisible(i < int(self.combo_players.currentText()))

    def get_players(self):
        return [self.line_edits[i].text() for i in range(int(self.combo_players.currentText()))]

    def get_start_money(self):
        return int(self.start_money.text())



