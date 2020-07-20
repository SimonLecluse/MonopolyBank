from PySide2.QtWidgets import QApplication
import sys
from src.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # creation de la CustomQDialog
    dialog = CustomQDialog()
    if dialog.exec_():
        c = Controller(dialog.get_players())

    sys.exit(app.exec_())