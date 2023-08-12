# -*- This python file uses the following encoding : utf-8 -*-

import time

from PySide6.QtMultimedia import QMediaCaptureSession, QAudioInput, QMediaRecorder
from PySide6.QtCore import QUrl

import utils


def start_recorder():
    global recorder

    #home_directory = utils.get_home_directory()
    file_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
    #path = f"{home_directory}/AR Intercom/Media/Voices/{file_name}"
    path = f"{file_name}.mp3"

    audio_input = QAudioInput()

    recorder = QMediaRecorder()
    recorder.setQuality(QMediaRecorder.Quality.HighQuality)
    recorder.setOutputLocation(QUrl.fromLocalFile(path))

    session = QMediaCaptureSession()
    session.setAudioInput(audio_input)
    session.setRecorder(recorder)

    recorder.record()
    #print(recorder.error())
    recorder.errorChanged.connect(lambda: print(recorder.error()))
    recorder.durationChanged.connect(lambda: print(recorder.duration()))
    #print("Recording...")



def pause_recorder():
    recorder.pause()
    print("Recording paused.")


def stop_recorder():
    recorder.stop()
    print("Recording done.")


# class Recorder(QMediaRecorder):
#     def __init__(self):
#         super().__init__()


