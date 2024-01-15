# -*- This python file uses the following encoding : utf-8 -*-

import os
import shutil
import sys
import socket
from functools import partial

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLineEdit
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QTimer

from gui.ui_register_window import Ui_SigninWindow
from styles import LineEdit, Features

from model.base import engine, db, Model
from model import User

from login_window import LoginWindow
import utils


class RegisterWindow(QWidget):
    """
    Register a new user on first app launch
    """
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SigninWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("AR Intercom - Sign up")

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # SET UP SHADOW
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 50))

        # Apply shadow on register window
        self.setGraphicsEffect(self.shadow)

        self.ui.choose_profilepicture.setToolTip("Photo de profile")

        # Create database
        Model.metadata.create_all(engine)

        # Initialize a new user
        self.user = User()
        self.user.set_uuid()

        # SET MOVE EVENT ON THE WINDOW
        self.dragPos = None
        self.ui.main_title.mouseMoveEvent = self.move_window

        # CONNECT CHOOSE PROFILE
        self.ui.choose_profilepicture.mousePressEvent = self.choose_profile

        # CONNECT "NEXT" AND "VALIDATE" BUTTONS
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

        # SHOW WINDOW
        self.show()

    def move_window(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos.toPoint())
            self.dragPos = event.globalPosition()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def go_back(self):
        """
        Return to the previous stacked widget page
        """
        index = self.ui.stackedWidget.currentIndex()

        if index != 0: self.ui.stackedWidget.setCurrentIndex(index - 1)
        if index == 1: self.ui.return_button.hide()

    def choose_profile(self, event):
        """
        Select a profile picture in a file dialog
        """
        if event.buttons() == Qt.MouseButton.LeftButton:
            picture_dialogue = QFileDialog.getOpenFileName(self, "Profile picture", utils.get_home_directory(), "Photos *.jpg *.png")
            path = picture_dialogue[0]

            if path:
                # Show image on the label
                rounded_pixmap = utils.create_rounded_image(path, self.ui.choose_profilepicture.height())
                self.ui.choose_profilepicture.setPixmap(rounded_pixmap)
                self.user.image_path = path

    def validate(self):
        """
        Verify if data where correctly entered by the user in the register window,
        in which case they ara saved in database
        """
        errors = []

        # CHECK LINES EDIT
        for widget in self.ui.form.findChildren(QLineEdit):
            if not widget.text():
                errors.append("1")
                widget.setStyleSheet(LineEdit.style_error)
            else:
                try:
                    errors.pop()
                except IndexError:
                    pass
                widget.setStyleSheet(LineEdit.style_normal)

        # CHECK IDENTICAL PASSWORDS
        if self.ui.passcode2.text() != self.ui.passcode.text():
            errors.append("1")
            self.ui.passcode2.setStyleSheet(LineEdit.style_error)
        else:
            try:
                errors.pop()
            except IndexError:
                pass
            self.ui.passcode2.setStyleSheet(LineEdit.style_normal)
            self.user.set_password(self.ui.passcode.text())

        # IF NECESSARY DATA IS COLLECTED, GO TO THE NEXT PAGE
        if len(errors) == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.return_button.show()

    def confirm_subscription(self):
        """
        Verify if user agrees to the terms of use then save his information in database
        """
        self.user.user_name = self.ui.user_name.text()
        self.user.phone = self.ui.phone.text()
        self.user.host_name = socket.gethostname()
        self.user.host_address = utils.get_private_ip()

        if self.ui.iaggree.isChecked():
            if self.user.image_path is not None:
                user_profile_path = os.path.join(utils.get_storage_path(),
                                f"{self.user.uuid.split('-')[0]}{os.path.splitext(self.user.image_path)[1]}")
                shutil.copyfile(self.user.image_path, user_profile_path)
                self.user.image_path = user_profile_path

            db.add(self.user)
            db.commit()

            self.ui.stackedWidget.setCurrentIndex(2)
            QTimer.singleShot(2900, lambda: self.ui.prev_feature.setStyleSheet(Features.prev))
            QTimer.singleShot(3000, lambda: self.ui.next_feature.setStyleSheet(Features.next))

            self.ui.return_button.hide()

    def features(self, page):
        """
        Navigate through feature pictures after registration
        """
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
                if self.ui.next_feature.isHidden():
                    self.ui.next_feature.show()

            elif index == 5:
                self.ui.next_feature.hide()
                if self.ui.prev_feature.isHidden():
                    self.ui.prev_feature.show()

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
        """
        Ends subscription process and go to log in window
        """
        # Close registration window
        self.close()

        # Show login window
        self.login_window = LoginWindow()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    register_window = RegisterWindow()
    sys.exit(app.exec())
