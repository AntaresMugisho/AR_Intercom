# -*- This python file uses the following encoding : utf-8 -*-
import sys
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QEasingCurve,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot, QTimer, QPropertyAnimation)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    Main window
    """
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI FUNCTIONS

        self.ui.left_menu.setFixedWidth(50)
        self.ui.right_stacked_widget.setFixedWidth(0)
        self.ui.emoji_widget.setFixedHeight(0)
        # self.ui.emoji_widget.setFixedWidth(0)

        self.ui.menu_btn.clicked.connect(self.toggle_menu)
        self.ui.settings_btn.clicked.connect(self.toggle_settings)
        self.ui.settings_btn_2.clicked.connect(self.toggle_settings)
        self.ui.emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.close_emoji_btn.clicked.connect(self.toggle_emojis)


    def toggle_settings(self):
        if self.ui.right_stacked_widget.width() == 0:
            start_value = 0
            end_value = 251
        else:
            start_value = 251
            end_value = 0

        # ANIMATION SETTINGS BOX
        self.animation = QPropertyAnimation(self.ui.right_stacked_widget, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation.start()


    def toggle_menu(self):
        if self.ui.left_menu.width() == 50:
            start_value = 50
            end_value = 168
        else:
            start_value = 168
            end_value = 50

        # ANIMATION MENU BOX
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation.start()


    def toggle_emojis(self):
        if self.ui.emoji_widget.height() == 0:
            self.ui.emoji_widget.setFixedHeight(206)
        else:
            self.ui.emoji_widget.setFixedHeight(0)


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
