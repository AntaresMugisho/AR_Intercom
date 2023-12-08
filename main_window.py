# -*- This python file uses the following encoding : utf-8 -*-

import sys

from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow, QWidget, QPushButton, QLabel, \
    QScrollArea, QGridLayout, QHBoxLayout, QVBoxLayout, QTabWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, Slot, QTimer, Qt
import EmojiStore

from gui import Ui_MainWindow
from widgets import Bubble, ClientWidget, DateLabel, EmojiButton
from functions import *

# Global variables for recorder time counter
# seconds = minutes = 0


class MainWindow(QMainWindow):
    """
    Main window
    """

    WINDOW_MAXIMIZED = False
    # DATE = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # REMOVE DEFAULT WINDOW FRAME
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.app_margins.setContentsMargins(0, 0, 0, 0)

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.app_bg.setGraphicsEffect(self.shadow)

        # HIDE ASIDE MENU TEXT, SETTINGS PANEL, EMOJI WIDGET AND MEDIA BUTTONS ON START UP
        self.ui.left_menu.setFixedWidth(60)
        self.ui.right_stacked_widget.setFixedWidth(0)
        self.ui.emoji_widget.setFixedHeight(0)
        self.ui.media_bg.setFixedHeight(0)
        self.ui.chat_page_layout.removeWidget(self.ui.media_bg)

        # CONNECT BUTTONS
        self.ui.menu_btn.clicked.connect(self.toggle_menu)
        self.ui.settings_btn.clicked.connect(self.toggle_settings)
        self.ui.emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.close_emoji_btn.clicked.connect(self.toggle_emojis)
        self.ui.media_btn.clicked.connect(self.toggle_media)

        # System buttons
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.maximize_restore_btn.clicked.connect(self.maximize_restore)
        self.ui.close_btn.clicked.connect(self.close)

        # Menus
        self.ui.home_btn.clicked.connect(self.menu_click)
        self.ui.scan_btn.clicked.connect(self.menu_click)
        self.ui.chat_btn.clicked.connect(self.menu_click)
        self.ui.about_btn.clicked.connect(self.menu_click)

        self.ui.chat_scroll_layout.itemAt(1).spacerItem()

        # Start on home page
        self.ui.home_btn.clicked.emit()

        # Initialize chat functions
        self.add_user_list()
        self.add_emojis()


        # SHOW MAIN WINDOW
        self.show()


    # MAIN UI FUNCTIONS ################################################################################################

    # def closeEvent(self, event) -> None:
    #     pass
        # try:
        #     ...
        # except Exception as e:
        #     print(f"Error while closing : ", e)

    def maximize_restore(self):
        """
        Minimize and restore the window size
        """
        if not self.WINDOW_MAXIMIZED:
            self.showMaximized()
            self.WINDOW_MAXIMIZED = True
            self.ui.maximize_restore_btn.setStatusTip("Restore")
            self.ui.maximize_restore_btn.setStyleSheet("background-image:url(:/cils/cils/icon_restore.png);")

        else:
            self.showNormal()
            self.WINDOW_MAXIMIZED = False
            self.ui.maximize_restore_btn.setStatusTip("Maximize")
            self.ui.maximize_restore_btn.setStyleSheet("background-image:url(:/cils/cils/icon_maximize.png);")

    @Slot()
    def menu_click(self):
        """
        Change view when the user clicks on a menu.
        """
        menu_btn: QPushButton = self.sender()
        menu = menu_btn.objectName()
        self.set_as_active(menu)

        if menu == "home_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.about_page)
            self.ui.chat_stacked_widget.setCurrentWidget(self.ui.home_page)

        elif menu == "scan_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.contact_page)
            self.ui.contacts_stack.setCurrentWidget(self.ui.scan_page)

        elif menu == "chat_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.contact_page)
            self.ui.contacts_stack.setCurrentWidget(self.ui.chat_list_page)

        elif menu == "about_btn":
            self.ui.left_side_container.setCurrentWidget(self.ui.about_page)

    def set_as_active(self, menu):
        """
        Change the active menu style.
        """
        selected_menu_style = """
            text-align:left;
            padding-left:42px;
            border-left:16px solid transparent;
            border-radius: 0px;
            background-repeat:none;
            background-position:center left;		
            border-left: 16px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.699 
                rgba(255, 200, 200, 255), stop:0.7 rgba(0, 0, 0, 0));
            background-color: rgb(40, 42, 43);
        """

        for btn in self.ui.left_menu.findChildren(QPushButton):
            if btn.objectName() == menu:
                btn.setStyleSheet(btn.styleSheet() + selected_menu_style)
            else:
                reset_style = btn.styleSheet().replace(selected_menu_style, "")
                btn.setStyleSheet(reset_style)

    def start_animation(self, widget, min, max):
        """
        Animate widget
        """
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
        """
        Show/Hide settings widget
        """
        self.start_animation(self.ui.right_stacked_widget, 0, 251)

    @Slot()
    def toggle_menu(self):
        """
        Show/Hide menu text
        """
        self.start_animation(self.ui.left_menu, 60, 168)

    # CONVERSATION SCREEN FUNCTIONS ####################################################################################

    @Slot()
    def toggle_emojis(self):
        """
        Show/Hide emoji list widget on chat screen
        """
        if self.ui.emoji_widget.height() == 0:
            self.ui.emoji_widget.setFixedHeight(196)
        else:
            self.ui.emoji_widget.setFixedHeight(0)

    @Slot()
    def toggle_media(self):
        """
        Show/Hide buttons to send media messages on chat screen
        """
        if self.ui.media_bg.height() == 0:
            self.ui.media_bg.move(QPoint(12, self.ui.chat_page.height() - 260))
            self.ui.media_bg.setFixedHeight(190)

        else:
            self.ui.media_bg.setFixedHeight(0)
            # self.ui.chat_page_layout.addWidget(self.ui.media_bg)

    def add_emojis(self):
        categories = ['smileys_and_people',
                      'animals_and_nature',
                      'food_and_drink',
                      'travel_and_places',
                      'activities',
                      'objects',
                      'symbols',
                      'flags'
        ]

        for i, category in enumerate(categories):
            tab: QTabWidget = self.ui.emoji_tab_widget.widget(i)
            scroll_area: QScrollArea = tab.findChild(QScrollArea)
            layout: QGridLayout = scroll_area.widget().layout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(2)

            # Delete default emoji button from the layout
            layout.itemAtPosition(0, 0).widget().deleteLater()

            row = 0
            column = -1
            for emoji in EmojiStore.get_by_category(category):
                column += 1
                if column % 24 == 0:
                    row += 1
                    column = 0
                btn = EmojiButton(emoji.emoji)
                layout.addWidget(btn, row, column)

    def add_user_list(self):
        """
        Load users conversation list from users who are registered in database
        """
        # Save spacer item
        chat_list_layout_count = self.ui.chat_list_layout.count()
        spacer = self.ui.chat_list_layout.itemAt(chat_list_layout_count - 1)

        # Remove old list
        for i in reversed(range(chat_list_layout_count - 1)):
            widget = self.ui.chat_list_layout.itemAt(i).widget()
            widget.deleteLater()
            self.ui.chat_list_layout.removeWidget(widget)

        # Add new user's list
        users = User.where("id", ">=", 1)
        for user in users:
            widget = ClientWidget(user)
            last_index = self.ui.chat_list_layout.count() - 1
            self.ui.chat_list_layout.insertWidget(last_index, widget, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignTop)
            widget.clicked.connect(self.show_conversations(self))

        # Add spacer
        self.ui.chat_list_layout.addItem(spacer)



if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
