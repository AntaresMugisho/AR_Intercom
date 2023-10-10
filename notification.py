# -*- This python file uses the following encoding : utf-8 -*-

import sys

from PySide6.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect
from PySide6.QtGui import QGuiApplication, QIcon, QPixmap, QColor
from PySide6.QtCore import QTimer, Qt

from gui.popup_window import Ui_NotificationWidget
from player import Player

class NotificationWidget(QWidget):

    def __init__(self, sender_name):
        QWidget.__init__(self)
        self.ui = Ui_NotificationWidget()
        self.ui.setupUi(self)
        self.sender_name = sender_name
        self.ui.title.setText("Nouveau message")
        self.ui.sender_name.setText(f"{self.sender_name} vous a envoyé un message !")

        # SET WINDOW ICON
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/icons/app_icon.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # DROP SHADOW
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(255, 0, 0, 100))

        # Apply shadow
        self.ui.global_frame.setGraphicsEffect(shadow)

        # SET POSITION OF THE NOTIFICATION WIDGET ON THE SCREEN
        screen_rect = QGuiApplication.primaryScreen().availableGeometry()

        if sys.platform == "win32":
            self.move(screen_rect.bottomRight().x() - 360, screen_rect.bottomRight().y() - 140)
        else:
            self.move(screen_rect.bottomRight().x() - 360, screen_rect.topRight().y() + 40)

        # PLAY A RINGTONE
        self.player = Player()
        self.player.volume(20)
        self.player._play("resources/ringtones/1.wav")

        # AUTO CLOSE NOTIFICATION WINDOW AFTER 4 SECONDS
        QTimer.singleShot(4_000, lambda: self.close())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NotificationWidget("Anta")
    widget.show()

    sys.exit(app.exec())


