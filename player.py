# -*- This python file uses the following encoding : utf-8 -*-

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl


class Player(QMediaPlayer):

    def __init__(self):
        super().__init__()

        # Audio output device
        self.audio_output = QAudioOutput()

        # Media player setup
        self.setAudioOutput(self.audio_output)

        self.errorOccurred.connect(lambda: print(self.error()))

    def _play(self, path="music.mp3"):
        try:
            self.stop()
        except Exception as e:
            print("Can't stop player: ", e)

        self.setSource(QUrl.fromLocalFile(path))
        self.play()

    def _pause(self):
        if self.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.pause()
        elif self.playbackState() == QMediaPlayer.PlaybackState.PausedState:
            self.play()

    def _stop(self):
        self.stop()
