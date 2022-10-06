# -*- This python file uses the following encoding : coding:utf-8 -*-

from Serveur import Serveur

print("\n██████ AR INTERCOM Beta ██████\n Designed by a Creative Mind.\n"
      "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

server = Serveur()
server.create_socket_server()
server.launch_server()