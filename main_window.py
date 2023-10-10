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

        # HIDE MENU TEXT AND SETTINGS PANEL ON START
        self.ui.left_menu.setFixedWidth(50)
        self.ui.right_stacked_widget.setFixedWidth(0)
        self.ui.emoji_widget.setFixedHeight(0)

        # CONNECT BUTTONS
        self.ui.menu_btn.clicked.connect(self.toggle_menu)
        self.ui.settings_btn.clicked.connect(self.toggle_settings)
        self.ui.settings_btn_2.clicked.connect(self.toggle_settings)
        self.ui.emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.close_emoji_btn.clicked.connect(self.toggle_emojis)

        # Menus
        self.ui.home_btn.clicked.connect(self.menu_click)
        self.ui.scan_btn.clicked.connect(self.menu_click)
        self.ui.contact_btn.clicked.connect(self.menu_click)
        self.ui.about_btn.clicked.connect(self.menu_click)

    @Slot()
    def menu_click(self):
        menu_clicked: QPushButton = self.sender()
        menu = menu_clicked.objectName()

        if menu == "home_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.about_page)
            self.ui.chat_stacked_widget.setCurrentWidget(self.ui.home_page)

        elif menu == "scan_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.contact_page)
            self.ui.contacts_stack.setCurrentWidget(self.ui.scan_page)

        elif menu == "contact_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.contact_page)
            self.ui.contacts_stack.setCurrentWidget(self.ui.chat_list_page)

        elif menu == "about_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.about_page)

    def start_animation(self, widget, min, max):
        if widget.width() == min:
            start_value = min
            end_value = max
        else:
            start_value = max
            end_value = min

        # ANIMATION SETTINGS BOX
        self.animation = QPropertyAnimation(widget, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(start_value)
        self.animation.setEndValue(end_value)
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation.start()

    @Slot()
    def toggle_settings(self):
        self.start_animation(self.ui.right_stacked_widget, 0, 251)

    @Slot()
    def toggle_menu(self):
        self.start_animation(self.ui.left_menu, 50, 168)

    @Slot()
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
