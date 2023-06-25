import socket
import threading
import subprocess

import utils
from users import Users

hosts = {}

class NetscanThread(threading.Thread):

    def __init__(self, address):
        threading.Thread.__init__(self)
        self.address = address

    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        reply = subprocess.call(["ping", "-c", "1", address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if reply == 0:
            try:
                hostname = socket.gethostbyaddr(address)
            except socket.herror:
                hostname = "Unknown"
            hosts[address] = hostname


if __name__ == "__main__":
    addresses = []
    threads = []

    my_ip = utils.get_private_ip()
    my_ip_bytes = my_ip.split(".")
    net_id = ".".join(my_ip_bytes[:3])

    for host_id in range(2, 255):  # 0 is supposed to be Net address, 1 the Gateway and 255 the Broadcast address
        if host_id != int(my_ip_bytes[3]):
            addresses.append(f"{net_id}.{str(host_id)}")

    netscanthreads = [NetscanThread(address) for address in addresses]
    for thread in netscanthreads:
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for address, hostname in hosts.items():
        # if (hostname != None):
        print(address, '=>', hostname)