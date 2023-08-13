# -*- This python file uses the following encoding : utf-8 -*-

import sys
import time
import threading

import sounddevice
import wavio
from PyQt6.QtWidgets import QApplication, QFrame, QLabel, QMessageBox, QSlider, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import QUrl, QTimer, QThread

from chat_window import ChatWindow
from styles import *


chrono, mins = (1, 0)


class Chat(ChatWindow):
    def __init__(self):
        super().__init__()



    def play_voice(self):


        def _state_changed(state):
            """
            Perform some actions according to the playing state
            """
            if state == QMediaPlayer.PlayingState:
                play_button.setStyleSheet(Player.pause)
                play_button.setToolTip("Pause")

            if state == QMediaPlayer.PausedState:
                play_button.setStyleSheet(Player.play)

            elif state == QMediaPlayer.StoppedState:
                self.player.setPosition(0)
                slider.setValue(0)
                play_button.setStyleSheet(Player.play)
                play_button.setObjectName("play_button")
                play_button.setToolTip("")

        # To prevent MacOS not support .arv format
        if sys.platform == "darwin":
            ext = ".wav"
        else:
            ext = ".arv"

        path = f"{self.home}/Documents/AR Intercom/Media/Voices/{voice_title}{ext}"

        self.player = QMediaPlayer()
        self.player.stateChanged.connect(_state_changed)

        self.player.error.connect(erroralert)


        slider.valueChanged.connect(self.player.setPosition)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Chat()
    sys.exit(app.exec())
