

import sys
from functools import partial

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout,\
    QPushButton, QListWidget, QListWidgetItem, QTabWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudioDevice
from PySide6.QtCore import QUrl
import emojis

import player
import recorder
from recorder import Recorder
from player import Player


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        categories = ["Smileys & Emotion", "Animals & Nature", "Food & Drink", "Travel & Places", "Activities", "Objects", "Symbols", "Flags"]
        tab_widget = QTabWidget()

        for category in categories:
            tab = QListWidget()
            for emoji in emojis.db.get_emojis_by_category(category):
               tab.addItem(QListWidgetItem(emoji.emoji))

            tab_widget.addTab(tab, f"{category}")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Window()
    run.show()
    sys.exit(app.exec())