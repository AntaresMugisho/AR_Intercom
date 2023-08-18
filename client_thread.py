

from PySide6.QtCore import QThread, QObject, Signal
from client import Client

class ClientThread(QThread):

    my_signal = Signal(str)

    def run(self):
        # Long task
        client = Client()

