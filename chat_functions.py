# -*- This python file uses the following encoding : utf-8 -*-

import sys
import time
import threading

import sounddevice
import wavio
from PyQt6.QtWidgets import QApplication, QFrame, QLabel, QMessageBox, QSlider, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import QUrl, QTimer, QThread

from chat_window import ChatWindow
from styles import *


chrono, mins = (1, 0)


class Chat(ChatWindow):
    def __init__(self):
        super().__init__()

    def resend_message(self):

        clicked = self.sender()
        parent = clicked.parent()

        for label in parent.findChildren(QLabel):
            if label.objectName() == "label_":
                text = label.text()

        parent.deleteLater()


    def play_voice(self):

        def hhmmss(ms):
            # s = 1000
            # m = 60000
            # h = 3600000
            h, r = divmod(ms, 3600000)
            m, r = divmod(r, 60000)
            s, _ = divmod(r, 1000)
            return ("%02d:%02d:%02d" % (h, m, s)) if h else ("%02d:%02d" % (m, s))

        def update_duration(duration):
            try:
                slider.setMaximum(duration)

                if duration >= 0:
                    total_time.setText(hhmmss(duration))
            except:
                pass

        def update_position(position):
            try:
                if position >= 0:
                    elapsed_time.setText(hhmmss(position))

                # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
                slider.blockSignals(True)
                slider.setValue(position)
                slider.blockSignals(False)

            except:
                pass

        def _state_changed(state):
            try:
                if state == QMediaPlayer.PlayingState:
                    play_button.setStyleSheet(Player.pause)
                    play_button.setToolTip("Pause")

                if state == QMediaPlayer.PausedState:
                    play_button.setStyleSheet(Player.play)

                elif state == QMediaPlayer.StoppedState:
                    self.player.setPosition(0)
                    slider.setValue(0)
                    play_button.setStyleSheet(Player.play)
                    play_button.setObjectName("play_button")
                    play_button.setToolTip("")
            except:
                pass

        def erroralert(*args):
            print(args)

        # STOP PLAYER IF PALAYING
        try:
            self.player.stop()
        except:
            pass

        #### GET WIDGETS FOR PLAY CLICKED BUTTON
        play_button = self.sender()
        parent = play_button.parent()

        # GET TITLE LABEL
        for widget in parent.findChildren(QLabel):
            if widget.objectName() == "media_":
                voice_title = widget.text()

            if widget.objectName() == "elapsed_time":
                elapsed_time = widget

            if widget.objectName() == "total_time":
                total_time = widget

        # GET SLIDER
        for widget in parent.findChildren(QSlider):
            slider = widget

        # To prevent MacOS not support .arv format
        if sys.platform == "darwin":
            ext = ".wav"
        else:
            ext = ".arv"

        path = f"{self.home}/Documents/AR Intercom/Media/Voices/{voice_title}{ext}"

        self.player = QMediaPlayer()
        self.player.stateChanged.connect(_state_changed)

        self.player.error.connect(erroralert)
        self.player.setMedia(QUrl.fromLocalFile(path))

        self.player.play()

        self.player.durationChanged.connect(update_duration)
        self.player.positionChanged.connect(update_position)

        slider.valueChanged.connect(self.player.setPosition)


    def record_voice(self):

        # DEFINE SOME FUNCTIONS
        def time_counter():

            global chrono, mins
            secs = chrono
            if secs > 0 and secs == 60:
                secs = 0
                mins += 1
                chrono = 0

            time = "%02d:%02d" % (mins, secs)
            self.record_time.setText(time)
            chrono += 1

            # Limit show recording time to secs
            if sys.platform == "darwin":
                if chrono > 20:
                    self.record_tip.deleteLater()
                    chrono, mins = (1, 0)

                    # stop timer
                    self.rec_timer.stop()
            else:
                if chrono > 7:
                    self.record_tip.deleteLater()
                    chrono, mins = (1, 0)

                    # stop timer
                    self.rec_timer.stop()

        def recorder():

            # AUDIO DURATION IN SECS AND CHANNEL
            self.frequency = 44100  # Sample rate
            duration = 6  # Recording duration

            # START RECORD
            self.record = sounddevice.rec(int(duration * self.frequency), samplerate=self.frequency, channels=2)
            print(f"Enregistrement en cours {duration} secondes max...")
            sounddevice.wait()
            self.th_rec.terminate()

        def save_record():
            """Saves the array records as file and try to send it"""

            # SAVE FILE
            directory = f"{self.home}/Documents/AR Intercom/Media/Voices/"

            # Renaming file
            self.ext = ".wav" if sys.platform == "darwin" else ".arv"
            self.file_output_name = f"ARV-{time.strftime('%d%m%Y-%H%M-%S')}"
            self.media_path = f"{directory}{self.file_output_name}{self.ext}"

            try:
                # Convert numpy array to arv(wav audio)
                wavio.write(self.media_path, self.record, self.frequency, sampwidth=2)

                # Send audio
                print("Enregistrement terminé.")
                self.send_media("voice", self.media_path)

            except Exception as e:
                print("Erreur 588FUNC: ", e)

        # -------------------------------------------------------------------------------

        addressee = self.ui.active_client.text()
        if not addressee:
            QMessageBox.warning(self.MainWindow, "Destinataire non défini",
                                "Veuillez spécifiez d'abord votre destinataire!",
                                QMessageBox.Ok)

        else:
            # RECORD TIME INDICATOR
            # > WIDGET
            self.record_widget()

            # > QTIMER
            self.rec_timer = QTimer()
            self.rec_timer.timeout.connect(time_counter)

            self.rec_timer.start(1000)

            # RECORD IN THREAD TO PREVENT GUI FREEZING
            # This thread (QThread) is to know the end of recording
            self.th_rec = QThread()
            self.th_rec.finished.connect(save_record)
            self.th_rec.start()

            self.thr = threading.Thread(target=recorder)
            self.thr.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Chat()
    sys.exit(app.exec())
