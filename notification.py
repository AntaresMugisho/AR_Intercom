# -*- This python file uses the following encoding : utf-8 -*-

import sys

from PySide6.QtWidgets import  QWidget, QApplication
from ui.popup_window import Ui_NotificationWidget


class NotificationWidget(QWidget):

    def __init__(self, sender_name):
        QWidget.__init__(self)
        self.ui = Ui_NotificationWidget()
        self.ui.setupUi(self)
        self.sender_name = sender_name
        self.ui.title.setText("Nouveau message")
        self.ui.sender_name.setText(f"{self.sender_name} vous a envoyé un message !")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NotificationWidget("Anta")
    widget.show()

    sys.exit(app.exec())


