# -*- This python file uses the following encoding : utf-8 -*-

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtCore import QUrl


class Player:

    def __init__(self):
        self.audio_output = QAudioOutput()

        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)

        self.player.errorChanged.connect(lambda: print(self.player.error()))

    def play(self, path="music.mp3"):
        # path = "music.mp3"
        self.player.setSource(QUrl.fromLocalFile(path))
        self.player.play()
        # self.player.hasAudioChanged()

    def pause(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        elif self.player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
            self.player.play()

    def stop(self):
        self.player.stop()
