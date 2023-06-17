# -*- This python file uses the following encoding : utf-8 -*-

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl


def _play():
    path = '/media/antares/6A1A45541A451F07/Phone/Clips/But na Filet/But na Filet/but_na_filet_amour_perdu_clip_officiel_h264_79541.mp3'

    audio_output = QAudioOutput()

    player = QMediaPlayer()
    player.setSource(QUrl.fromLocalFile(path))
    player.setAudioOutput(audio_output)
    audio_output.setVolume(30)
    print(audio_output.volume())
    player.play()
    print(audio_output.volume())
