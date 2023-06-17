# -*- This python file uses the following encoding : utf-8 -*-

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl


def _play():
    path = 'music.mp3'

    player = QMediaPlayer()
    audio_output = QAudioOutput()
    player.setAudioOutput(audio_output)
    player.setSource(QUrl.fromLocalFile(path))
    #audio_output.setVolume(0.5)
    player.play()
    player.errorChanged.connect(lambda: print(player.error()))

