

import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudioDevice
from PySide6.QtCore import QUrl

import player
import recorder
from recorder import *
from player import Player


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.setWindowTitle("Hello world")

        player = Player()

        vlayout = QVBoxLayout()
        self.setLayout(vlayout)

        play_btn = QPushButton("Play audio")
        play_btn.clicked.connect(partial(player.play))

        pause_btn = QPushButton("Pause audio")
        pause_btn.clicked.connect(player.pause)

        start_record_btn = QPushButton("Start record")
        start_record_btn.clicked.connect(recorder.start_recorder)

        stop_record_btn = QPushButton("Stop record")
        stop_record_btn.clicked.connect(recorder.stop_recorder)

        vlayout.addWidget(play_btn)
        vlayout.addWidget(pause_btn)
        vlayout.addWidget(start_record_btn)
        vlayout.addWidget(stop_record_btn)


        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Window()
    sys.exit(app.exec())