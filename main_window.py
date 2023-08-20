# -*- This python file uses the following encoding : utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())