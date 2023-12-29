# -*- This python file uses the following encoding : utf-8 -*-

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Signal, QObject


class Player(QMediaPlayer):

    def __init__(self):
        super().__init__()

        # Audio output device
        self.audio_output = QAudioOutput()

        # Media player setup
        self.setAudioOutput(self.audio_output)

        self.errorOccurred.connect(lambda error: print(error))

    def _play(self, path):
        self.setSource(QUrl.fromLocalFile(path))
        self.play()

    def _pause(self):
        if self.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.pause()
        elif self.playbackState() == QMediaPlayer.PlaybackState.PausedState:
            self.play()

    def volume(self, value):
        self.audio_output.setVolume(value/100)