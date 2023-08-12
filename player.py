# -*- This python file uses the following encoding : utf-8 -*-

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtCore import QUrl


class Player:

    def __init__(self):
        self.audio_output = QAudioOutput()

        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)

        self.player.errorChanged.connect(lambda: print(self.player.error()))
        # self.player.positionChanged.connect(lambda: print(self.player.position()))
        self.player.playbackStateChanged.connect(lambda: print(self.player.playbackState()))

    def play(self):
        path = "music.mp3"
        self.player.setSource(QUrl.fromLocalFile(path))
        self.player.play()
        # self.player.hasAudioChanged()

    def pause(self):
        print(self.player.playbackState())
        # if self.player.playbackState() == PlaybackState.PlayingState
        # self.player.pause()
