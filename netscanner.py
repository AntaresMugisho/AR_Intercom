

import sys
import socket
from PySide6.QtCore import QThread, QTimer, QRunnable, QThreadPool, QObject, Signal, Slot
from PySide6.QtWidgets import QApplication

import utils


class NetScannerSignals(QObject):
    """
    Defines the signals available from the running worker thread
    """
    finished = Signal()
    hosts = Signal(list)
    error = Signal(tuple)


class NetScanner(QRunnable):
    """
    Thread to regularly scan the network by pinging addresses
    """
    hosts = {}
    hosts = []

    def __init__(self):
        QRunnable.__init__(self)
        self.signals = NetScannerSignals()

    @Slot()
    def run(self):
        hosts = self.lookup()
        self.signals.hosts.emit(hosts)
        self.signals.finished.emit()

    def lookup(self):
        """
        Ping the given address and try to get more data if the address is alive
        """
        my_ip = utils.get_private_ip()
        if my_ip.startswith("127.0"):
            print("Aucun réseau détecté.\nVeuillez vous connecter à un réseau !")

        else:
            my_ip_bytes = my_ip.split(".")
            net_id = ".".join(my_ip_bytes[:3])

            for host_id in range(1, 255):  # 0 is supposed to be Net address, 1 the Gateway and 255 the Broadcast address
                # if host_id != int(my_ip_bytes[3]):
                address = f"{net_id}.{host_id}"
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # sock.settimeout(1)
                sock.connect((address, 33511))
                # sock.settimeout(None)
                NetScanner.hosts.append(address)
                # hostname, _, _ = socket.gethostbyaddr(address)
                # NetScanner.hosts[address] = hostname
            except TimeoutError:
                pass
            # else:
                # pass

        return NetScanner.hosts


if __name__ == "__main__":
    app = QApplication(sys.argv)

    scanner = NetScanner()
    scanner.signals.finished.connect(lambda: print("I'm done"))
    scanner.signals.hosts.connect(lambda h: print(h))

    thread_pool = QThreadPool()
    thread_pool.start(scanner)

    app.exec()
