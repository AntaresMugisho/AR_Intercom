

import sys
import socket
from PySide6.QtCore import QThread, QTimer, QRunnable, QThreadPool, QObject, Signal, Slot
from PySide6.QtWidgets import QApplication

import utils


class NetScannerSignals(QObject):
    """
    Defines the signals available from the running worker thread
    """
    # finished = Signal()
    hosts = Signal(list)
    error = Signal(tuple)
    host = Signal(str)


class NetScanner(QThread):
    """
    Thread to regularly scan the network by pinging addresses
    """
    # hosts = {}
    hosts = []

    def __init__(self, address):
        QThread.__init__(self)
        self.signals = NetScannerSignals()
        self.address = address

    @Slot()
    def run(self):
        hosts = self.lookup(self.address)
        self.signals.host.emit(self.address)
        # self.signals.finished.emit()

    def lookup(self, address):
        """
        Ping the given address and try to get more data if the address is alive
        """

        try:
            # print(f"[*] Reaching {address} ...")
            hostname, _, _ = socket.gethostbyaddr(address)
            # NetScanner.hosts[address] = hostname
            NetScanner.hosts.append(address)
        except socket.herror:
            pass

        return NetScanner.hosts


if __name__ == "__main__":
    app = QApplication(sys.argv)

    my_ip = utils.get_private_ip()
    if my_ip.startswith("127.0"):
        print("Aucune connexion détectée.\nVeuillez vous connecter à un réseau !")

    else:
        my_ip_bytes = my_ip.split(".")
        net_id = ".".join(my_ip_bytes[:3])

        threads = []
        for host_id in range(1, 255):  # 0 is supposed to be Net address, 1 the Gateway and 255 the Broadcast address
            # if host_id != int(my_ip_bytes[3]):
            address = f"{net_id}.{host_id}"
            scanner = NetScanner(address)
            scanner.signals.host.connect(lambda h: print(f"Scanning done for host {h}"))

            threads.append(scanner)

        # Start threads
        for scanner in threads:
            scanner.start()

    app.exec()
