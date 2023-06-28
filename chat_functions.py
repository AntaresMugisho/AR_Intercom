# -*- This python file uses the following encoding : utf-8 -*-

import sys
import sqlite3
import time
import threading

import sounddevice
import wavio
from PyQt6.QtWidgets import QApplication, QFrame, QLabel, QMessageBox, QSlider, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import QUrl, QTimer, QThread

from chat_window import ChatWindow
from users import Users
from styles import *
import utils
from client import Client

chrono, mins = (1, 0)


class Chat(ChatWindow):
    def __init__(self):
        super().__init__()

        # CREATE MEDIA FOLDERS IF NOT EXISTS
        utils.create_media_folders()

    def send_message(self, resending=None):
        """Send the message to the active client and shows the right bubble."""

        addressee = self.ui.active_client.text()

        if not addressee:
            QMessageBox.warning(self.MainWindow, "Destinataire non défini",
                                "Veuillez spécifiez d'abord votre destinataire!",
                                QMessageBox.Ok)

        send_time = time.strftime("%d-%m-%Y %H:%M")

        if not resending:
            message = self.entry_field.text()
        else:
            message = resending

        # SEND MESSAGE
        self.client.send_message("string", message)

        # Check status (feature)
        try:
            sent = int(self.client.status)
            self.check_online(self.ui.active_client.text())
        except Exception as e:
            print(f"Erreur 310 FUNC : {e}")

        # SHOW MESSAGE IN BUBBLE
        self.create_right_bubble("string", None, None, message, send_time, sent)
        self.entry_field.setText("")

        # SAVE MESSAGE
        client_table = "sa" + addressee[:2].lower() + "ch"
        self.save_message(client_table, "S", "string", None, ".str", message, send_time, sent)

    def resend_message(self):
        try:
            clicked = self.sender()
            parent = clicked.parent()

            connection = sqlite3.connect("sach.db")
            cursor = connection.cursor()

            table = "sa" + self.ui.active_client.text()[:2].lower() + "ch"

            for label in parent.findChildren(QLabel):
                if label.objectName() == "label_":
                    text = label.text()

                    cursor.execute(f"DELETE FROM {table} WHERE str = ?", (text,))
                    cursor.close()
                    connection.commit()
                    connection.close()

                    self.send_message(label.text())

                elif label.objectName() == "media_":
                    title = label.text()
                    cursor.execute(f"SELECT * FROM {table} WHERE title = ?", (title,))

                    req = cursor.fetchone()
                    kind = req[2]
                    extension = req[4]

                    cursor.execute(f"DELETE FROM {table} WHERE title = ?", (title,))
                    cursor.close()

                    connection.commit()
                    connection.close()

                    path = f"{self.home}/Documents/AR Intercom/Media/{kind.capitalize()}s/{title}{extension}"
                    self.send_media(kind, path)

            parent.deleteLater()

        except Exception as e:
            print("Erreur 380FUNC", e)

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

    def save_message(self, table, exp, kind, title, format, body, time, status):

        # TRY TO CONNECT TO THE DATABASE
        try:
            connection = sqlite3.connect("sach.db")
            cursor = connection.cursor()

            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table} (
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   exp TEXT NOT NULL,
                                   kind TEXT NOT NULL,
                                   title TEXT, 
                                   format TEXT NOT NULL,
                                   str TEXT,
                                   byte BLOB,
                                   time TEXT,
                                   status TEXT)""")

            # DEFINE DATA AND INSERT IT INTO TABLE
            if kind == "string":
                data = (exp, kind, None, format, body, None, time, status)
            else:
                data = (exp, kind, title, format, None, body, time, status)

            cursor.execute(f"INSERT INTO {table} (exp, kind, title, format, str, byte, time, status)"
                           " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)

            # SAVE CHANGES
            connection.commit()

            # CLOSE CONNECTION
            cursor.close()
            connection.close()

        except Exception as e:
            print("Erreur [511FUNC] : ", e)

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



    def receive(self, kind):
        """Shows the received message in a bubble."""

        # FORMAT MESSAGE
        message = self.server.received_message[
                  2:]  # the first and the second characters of msg are programm indicators.
        receive_time = time.strftime("%d-%m-%Y %H:%M")

        # SHOW MESSAGE IF SENDER IS ACTIVE ELSE SAVE IT
        active_client = self.ui.active_client.text()

        if active_client != "" and self.server.received_message[0] == active_client[0]:
            client_table = "sa" + active_client[:2].lower() + "ch"

            if kind == "string":

                # Show text message and save it
                self.create_left_bubble("string", None, None, message, receive_time)
                self.save_message(client_table, "R", "string", None, ".str", message, receive_time, True)

            else:
                title = self.server.media_info["Title"]
                extension = self.server.media_info["Extension"]
                blob = self.server.data

                # Show media message and save it
                self.create_left_bubble("voice", title, extension, blob, receive_time)
                self.save_message(client_table, "R", "voice", title, extension, None, receive_time, True)
        else:
            self.put_inbox(self.server.received_message, receive_time)

        # SHOW NOTIFICATION IN ALL CASES
        for name in Users.ulist:

            if name[0] == self.server.received_message[0]:  # If the initial letters are the same
                # Show popup -> From popup.py
                # popup = Popup(name)
                pass

    def put_inbox(self, message, time):
        for name in Users.ulist:

            if name[0] == message[0]:  # If the initial letters are the same

                # Increase message counter
                self.update_counter(name)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Chat()
    sys.exit(app.exec())
