# -*- This python file uses the following encoding : utf-8 -*-
import os
import time

from PySide6.QtMultimedia import QMediaCaptureSession, QAudioInput, QMediaRecorder
from PySide6.QtCore import QUrl, QFile, Signal

import utils


class Recorder(QMediaRecorder):

    recordConfirmed = Signal(str, str)

    def __init__(self):
        super().__init__()

        # Audio output device
        self.audio_input = QAudioInput()

        # Audio recorder setup
        self.setQuality(QMediaRecorder.Quality.HighQuality)

        # Capture session setup
        self.session = QMediaCaptureSession()
        self.session.setAudioInput(self.audio_input)
        self.session.setRecorder(self)

        self.errorOccurred.connect(lambda: print(self.error()))
        self.recorderStateChanged.connect(lambda: print(self.recorderState()))

    def _record(self):
        """
        Starts recording and save file in the specified directory
        """
        print("Recording...")
        home_directory = utils.get_home_directory()
        file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
        path = f"{home_directory}/AR_Intercom/Media/Voices/{file_name}"

        self.setOutputLocation(QUrl.fromLocalFile(path))
        self.record()

    def _pause(self):
        """
        Toggle between Play/Pause states of recorder
        """
        if self.recorderState() == QMediaRecorder.RecordingState:
            print("Recording paused.")
            self.pause()
        elif self.recorderState() == QMediaRecorder.PausedState:
            print("Continuing recorder")
            self.record()

    def _stop(self):
        """
        Stop recording
        """
        print("Recording done.")
        self.stop()
        # Emit confirmation with message details
        self.recordConfirmed.emit("voice", self.actualLocation().path()[1:])

    def cancel(self):
        """
        Stop recording and delete recorded file
        """
        print("Recording cancelled by user")
        self.stop()
        file = QFile(self.actualLocation().path()[1:])

        print(file.exists())
        file.remove()
        print(file.exists())

