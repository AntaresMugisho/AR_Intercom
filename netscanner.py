

import sys
import socket
from threading import Thread
from PySide6.QtCore import QThread, QTimer, QRunnable, QThreadPool, QObject, Signal, Slot
from PySide6.QtWidgets import QApplication

import utils


class NetScannerSignals(QObject):
    """
    Defines the signals available from the running worker thread
    """
    # Signal emitted after a network scan, returning an IP -> hostname dictionary of online hosts
    scanFinished = Signal(dict)


class NetScanner(Thread):
    """
    Thread to regularly scan the network by pinging addresses
    """

    COUNTER = 0
    hosts = {}

    def __init__(self, address):
        Thread.__init__(self)
        self.address = address

        # Create signals
        self.signal = NetScannerSignals()

    @Slot()
    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        """
        Ping the given address and try to get more data if the address is alive
        """

        try:
            hostname, _, _ = socket.gethostbyaddr(address)
            NetScanner.hosts[address] = hostname
        except socket.herror:
            NetScanner.hosts[address] = None

        finally:
            NetScanner.COUNTER += 1
            if NetScanner.COUNTER == 254:
                self.signal.scanFinished.emit(NetScanner.hosts)



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
            scanner.signal.scanFinished.connect(lambda h: print(h))

            threads.append(scanner)

        # Start threads
        for scanner in threads:
            scanner.start()

    app.exec()
