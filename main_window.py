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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame, QGraphicsDropShadowEffect,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    Main window
    """

    WINDOW_MAXIMIZED = False

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # REMOVE DEFAULT WINDOW FRAME
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.app_margins.setContentsMargins(0, 0, 0, 0)

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bg_app.setGraphicsEffect(self.shadow)

        # HIDE MENU TEXT AND SETTINGS PANEL ON START
        self.ui.left_menu.setFixedWidth(60)
        self.ui.right_stacked_widget.setFixedWidth(0)
        self.ui.emoji_widget.setFixedHeight(0)

        # CONNECT BUTTONS
        self.ui.menu_btn.clicked.connect(self.toggle_menu)
        self.ui.settings_btn.clicked.connect(self.toggle_settings)
        self.ui.settings_btn_2.clicked.connect(self.toggle_settings)
        self.ui.emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.close_emoji_btn.clicked.connect(self.toggle_emojis)

        # System buttons
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.min_max_btn.clicked.connect(self.maximize_restore)
        self.ui.close_btn.clicked.connect(self.close)

        # Menus
        self.ui.home_btn.clicked.connect(self.menu_click)
        self.ui.scan_btn.clicked.connect(self.menu_click)
        self.ui.contact_btn.clicked.connect(self.menu_click)
        self.ui.about_btn.clicked.connect(self.menu_click)

        # Start on home page
        # self.ui.home_btn.clicked.emit()

    def closeEvent(self, event) -> None:
        pass
        # messagebox = QMessageBox.question(self, "Close", "Do you really want to close the application ?",
        #                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        # if messagebox == QMessageBox.StandardButton.Yes:
        #     print("Close")
        # else:
        #     print("Don't close")

    def maximize_restore(self):

        if not self.WINDOW_MAXIMIZED:
            self.showMaximized()
            self.WINDOW_MAXIMIZED = True
            self.ui.min_max_btn.setStatusTip("Restore")

        else:
            self.showNormal()
            self.WINDOW_MAXIMIZED = False
            self.ui.min_max_btn.setStatusTip("Maximize")


    @Slot()
    def menu_click(self):
        menu_btn: QPushButton = self.sender()
        menu = menu_btn.objectName()
        self.set_as_active(menu)

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

    def set_as_active(self, menu):
        selected_menu_style = """
            text-align:left;
            padding-left:42px;
            border-left:16px solid transparent;
            border-radius: 0px;
            background-repeat:none;
            background-position:center left;		
            border-left: 16px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.699 rgba(255, 200, 200, 255), stop:0.7 rgba(0, 0, 0, 0));
            background-color: rgb(40, 42, 43);
        """

        for btn in self.ui.left_menu.findChildren(QPushButton):
            if btn.objectName() == menu:
                btn.setStyleSheet(btn.styleSheet() + selected_menu_style)
            else:
                reset_style = btn.styleSheet().replace(selected_menu_style, "")
                btn.setStyleSheet(reset_style)


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
        self.start_animation(self.ui.left_menu, 60, 168)

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
