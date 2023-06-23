import socket
import threading

import utils
from users import Users


class NetscanThread(threading.Thread):

    host = {}

    def __init__(self, address):
        threading.Thread.__init__(self)
        self.address = address
        self.addresses = []

    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        ip =  utils.get_private_ip()
        net_id = ".".join(ip.split(".")[:3])

        for host_id in range(256):
            self.addresses.append(f"{net_id}.{str(host_id)}")

        try:
            hostname, alias, _ = socket.gethostbyaddr(address)
            self.host[address] = hostname
        except socket.herror:
            self.host[address] = None


if __name__ == '__main__':
    addresses = []

    threads = []

    """ On créée autant de threads qu'il y à d'adresses IP à scanner """
    netscanthreads = [NetscanThread(address) for address in addresses]
    for thread in netscanthreads:
        """ Chaque thread est démarré en même temps """
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    """ On affiche le résultat qui affiche pour chaque machine connectée son nom d'hôte """

    for address, hostname in host.items():
        # if (hostname != None):
            #if not "home" in hostname:
        print(address, '=>', hostname)





