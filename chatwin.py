

# GUI FILE ########################################""
from chatwindow import Ui_ChatWindow

import sys
import platform

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import *   # import of all widgets (QApplication, QLabel ...)

###################################################################################

class UserInterface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)

        # SHOW WINDOW
        self.show()
        self.ui.online_toast_2.hide()


# MAIN PROGRAMM
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface()
    sys.exit(app.exec_())