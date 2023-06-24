import socket
import threading

import utils
from users import Users


class NetscanThread(threading.Thread):

    host = {}

    def __init__(self, address):
        threading.Thread.__init__(self)
        self.address = address

    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        try:
            hostname, alias, _ = socket.gethostbyaddr(address)
            self.host[address] = hostname
        except socket.herror:
            self.host[address] = None


