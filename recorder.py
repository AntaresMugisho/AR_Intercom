# -*- This python file uses the following encoding : utf-8 -*-

import time

from PySide6.QtMultimedia import QMediaCaptureSession, QAudioInput, QMediaRecorder
from PySide6.QtCore import QUrl

import utils


class Recorder:

    def __init__(self):



        # Audio output device
        self.audio_input = QAudioInput()

        # Audio recorder setup
        self.recorder = QMediaRecorder()
        self.recorder.setQuality(QMediaRecorder.Quality.HighQuality)

        # Capture session setup
        self.session = QMediaCaptureSession()
        self.session.setAudioInput(self.audio_input)
        self.session.setRecorder(self.recorder)

        self.recorder.errorChanged.connect(lambda: print(self.recorder.error()))
        self.recorder.errorOccurred.connect(lambda : print(self.recorder.error()))
        self.recorder.recorderStateChanged.connect(lambda: print(self.recorder.recorderState()))

    def start(self):
        print("Recording...")
        home_directory = utils.get_home_directory()
        file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
        # path = f"{home_directory}/AR Intercom/Media/Voices/{file_name}"
        path = f"{file_name}.mp3"

        self.recorder.setOutputLocation(QUrl.fromLocalFile(path))
        self.recorder.record()
        print(self.recorder.actualLocation())

    def pause(self):
        print("Recording paused.")
        self.recorder.pause()

    def stop(self):
        print("Recording done.")
        self.recorder.stop()
