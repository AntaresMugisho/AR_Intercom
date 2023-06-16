# -*- This python file uses the following encoding : utf-8 -*-

import socket
import select
import threading


class Server:
    """
    Server to listen, accept connections and receive text messages and files from other connected devices.
    """

    # ONLINE CLIENTS LIST
    CONNECTED_CLIENTS = []
    CONNECTED_CLIENTS_IPS = []

    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 12000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def accept_connections(self):
        """
        Accept all incoming connections
        """
        while True:
            try:
                rlist, wlist, xlist = select.select([self.sock], [], [], 0.50)
                for connection in rlist:
                    client, ip_address = connection.accept()
                    self.CONNECTED_CLIENTS.append(client)
                    self.CONNECTED_CLIENTS_IPS.append(ip_address[0])
            except Exception as e:
                print("Error in server :", e)
                break

    def start(self):
        """
        Launch socket server and accept incoming connections.
        """
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        thread = threading.Thread(target=self.accept_connections)
        thread.start()

    def stop(self):
        """
        Close socket server.
        """
        self.sock.close()
        print("Server closed !")


if __name__ == "__main__":
    server = Server()
    server.start()
