from PySide2.QtWidgets import QApplication
import sys
from src.controller import Controller
from src.view.dialog import CustomDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # creation de la CustomQDialog
    dialog = CustomDialog()
    if dialog.exec_():
        c = Controller(dialog.get_players(), dialog.get_start_money())

    sys.exit(app.exec_())