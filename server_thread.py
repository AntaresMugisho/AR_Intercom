

from PySide6.QtCore import QThread, QObject, Signal
from server import Server

class SereverThread(QThread):

    my_signal = Signal(str)

    def run(self):
        # Long task
        result = "Hello server"
        self.my_signal.emit(result)

        # Will call the Server's start() method here