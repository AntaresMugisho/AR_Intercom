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

        def hhmmss(ms: int):
            """
            Converts millisecond time in hour, minute and seconds
            """
            h, r = divmod(ms, 3_600_000)
            m, r = divmod(r, 60_000)
            s, _ = divmod(r, 1000)
            return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%02d:%02d" % (m, s))

        def update_duration(duration):
            slider.setMaximum(duration)
            if duration >= 0:
                total_time.setText(hhmmss(duration))


        def update_position(position):
            """
            Update playing media position by moving the slider
            """
            if position >= 0:
                elapsed_time.setText(hhmmss(position))

            # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
            slider.blockSignals(True)
            slider.setValue(position)
            slider.blockSignals(False)


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

        def erroralert(*args):
            print(args)

        # STOP PLAYER IF PALAYING
        try:
            self.player.stop()
        except:
            pass

        #### GET WIDGETS FOR PLAY CLICKED BUTTON
        play_button = self.sender()
        parent = play_button.parent()

        # GET TITLE LABEL
        for widget in parent.findChildren(QLabel):
            if widget.objectName() == "media_":
                voice_title = widget.text()

            if widget.objectName() == "elapsed_time":
                elapsed_time = widget

            if widget.objectName() == "total_time":
                total_time = widget

        # GET SLIDER
        for widget in parent.findChildren(QSlider):
            slider = widget

        # To prevent MacOS not support .arv format
        if sys.platform == "darwin":
            ext = ".wav"
        else:
            ext = ".arv"

        path = f"{self.home}/Documents/AR Intercom/Media/Voices/{voice_title}{ext}"

        self.player = QMediaPlayer()
        self.player.stateChanged.connect(_state_changed)

        self.player.error.connect(erroralert)
        self.player.setMedia(QUrl.fromLocalFile(path))

        self.player.play()

        self.player.durationChanged.connect(update_duration)
        self.player.positionChanged.connect(update_position)

        slider.valueChanged.connect(self.player.setPosition)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Chat()
    sys.exit(app.exec())
