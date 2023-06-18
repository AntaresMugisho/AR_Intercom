# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import sqlite3
from functools import partial

from PyQt6.QtWidgets import QApplication, QFileDialog, QPushButton, QLineEdit
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap

from register_window import RegisterWindow
from users import Users
from styles import LineEdit, ComboBox, Features


class Register(RegisterWindow):

    def __init__(self):
        # Initialize register window, containing register_window property
        RegisterWindow.__init__(self)

        self.data = []
        self.picture = None
        self.dragPos = None

        # SET MOVE EVENT ON THE WINDOW
        self.ui.main_title.mouseMoveEvent = self.move_window

        # CONNECT CHOOSE PROFILE
        self.ui.choose_profilepicture.mousePressEvent = self.choose_profile

        # CONNECT "NEXT" ADN "VALIDATE" BUTTON
        self.ui.next.clicked.connect(self.validate)
        self.ui.validate.clicked.connect(self.confirm_subscription)

        # HIDE "BACK" BUTTON ON START
        self.ui.return_button.clicked.connect(self.go_back)
        self.ui.return_button.hide()

        # INDICATE CURRENT FEATURE INDEX (0)
        self.ui.prev_feature.hide()
        self.ui.feature_0.setStyleSheet(Features.style_active)

        # CONNECT FEATURE BUTTONS AND HIDE THEM
        self.ui.next_feature.clicked.connect(partial(self.features, "Next"))
        self.ui.prev_feature.clicked.connect(partial(self.features, "Previous"))

        # Connect small indicators
        self.ui.feature_0.clicked.connect(partial(self.features, 0))
        self.ui.feature_1.clicked.connect(partial(self.features, 1))
        self.ui.feature_2.clicked.connect(partial(self.features, 2))
        self.ui.feature_3.clicked.connect(partial(self.features, 3))
        self.ui.feature_4.clicked.connect(partial(self.features, 4))
        self.ui.feature_5.clicked.connect(partial(self.features, 5))

        # CONNECT "TERMINATE" BUTTON
        self.ui.terminate.clicked.connect(self.terminate)

    def move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == 16777216:     # esc key
            self.close()

    def save_data(self, data):
        """
        Create a new table and insert new registered user data inside.
        """
        try:
            connection = sqlite3.connect("ui.db")
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS uidb (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    code TEXT NOT NULL,
                    psw TEXT,
                    pic BLOB,
                    port INTEGER NOT NULL)
            """)

            cursor.execute("INSERT INTO uidb (name, code, psw, pic, port) VALUES (?, ?, ?, ?, ?)", data)

            # SAVE AND CLOSE CONNEXION
            connection.commit()
            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error while saving: {e}")

    def go_back(self):
        index = self.stackedWidget.currentIndex()

        if index != 0: self.stackedWidget.setCurrentIndex(index - 1)
        if index == 1: self.return_button.hide()

    def choose_profile(self, event):
        if event.button() == 1:

            if sys.platform == "win32":
                home = os.environ["USERPROFILE"]
            else:
                home = os.environ["HOME"]

            self.picture = QFileDialog.getOpenFileName(self, "Profile picture", home, "Photos *.jpg *.PNG")
            directory = self.picture[0]
            if directory != "":

                # SET ICON TO LABEL
                self.ui.choose_profilepicture.setPixmap(QPixmap(directory))

                # CATCH BINARY
                with open(directory, "rb") as file:
                    self.picture = file.read()

    def validate(self):
        """
        Verify if data where correctly entered by the user in the register window,
        in which case they ara saved in database
        """

        server_port = ""

        # CHECK LINES EDIT
        for widget in self.ui.form.findChildren(QLineEdit):
            if not widget.text():
                widget.setStyleSheet(LineEdit.style_error)
            else:
                widget.setStyleSheet(LineEdit.style_normal)
                if widget.objectName() == "user_name":
                    self.data.append(self.ui.user_name.text())

        # CHECK COMBO BOX
        if self.ui.code.currentIndex() == 0:
            self.ui.code.setStyleSheet(ComboBox.style_error)
        else:
            self.ui.code.setStyleSheet(ComboBox.style_normal)
            user_code = self.ui.code.currentText()
            self.data.append(user_code)
            server_port = Users.dictionnary.get(user_code)

        # CHECK IDENTICAL PASSWORDS
        if self.ui.passcode2.text() != self.ui.passcode.text():
            self.ui.passcode2.setStyleSheet(LineEdit.style_error)
        else:
            self.ui.passcode2.setStyleSheet(LineEdit.style_normal)
            passcode = self.ui.passcode2.text()
            self.data.append(passcode)

        # CHECK PROFILE PICTURE
        try:
            if self.picture:
                if type(self.picture) == bytes:
                    self.data.append(self.picture)
                else:
                    self.data.append(None)
        except AttributeError:
            self.data.append(None)

        # ASSIGN PORT
        self.data.append(server_port)

        # IF ALL DATA IS COLLECTED, GO TO THE NEXT PAGE
        if len(self.data) == 5:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.return_button.show()

    def confirm_subscription(self):
        """
        Verify if user agrees to the terms of use
        """
        if self.ui.iaggree.isChecked():
            self.save_data(self.data)
            self.ui.stackedWidget.setCurrentIndex(2)
            try:
                QTimer.singleShot(2900, lambda: self.ui.prev_feature.setStyleSheet(Features.prev))
                QTimer.singleShot(3000, lambda: self.ui.next_feature.setStyleSheet(Features.next))
            except Exception as e:
                print(e)
            self.ui.return_button.hide()

    def features(self, page):
        index = self.ui.what_isnew.currentIndex()

        if page == "Next":
            index += 1
            self.ui.what_isnew.setCurrentIndex(index)
            if self.ui.prev_feature.isHidden():
                self.ui.prev_feature.show()

            if index == 5:
                self.ui.next_feature.hide()

        elif page == "Previous":
            index -= 1
            self.ui.what_isnew.setCurrentIndex(index)
            if self.ui.next_feature.isHidden():
                self.ui.next_feature.show()

            if index == 0:
                self.ui.prev_feature.hide()
        else:
            index = page
            self.ui.what_isnew.setCurrentIndex(index)

            if index == 0:
                self.ui.prev_feature.hide()
                if self.ui.next_feature.isHidden(): self.next_feature.show()

            elif index == 5:
                self.ui.next_feature.hide()
                if self.ui.prev_feature.isHidden(): self.ui.prev_feature.show()

            else:
                if self.ui.next_feature.isHidden(): self.ui.next_feature.show()
                if self.ui.prev_feature.isHidden(): self.ui.prev_feature.show()

        # Show current index
        for i, button in enumerate(self.ui.current_feature.findChildren(QPushButton)):
            if i == index:
                button.setStyleSheet(Features.style_active)
            else:
                button.setStyleSheet(Features.style_inactive)

    def terminate(self):
        # self.main = ChatWin()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Register()
    sys.exit(app.exec())
