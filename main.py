# -*- coding:utf-8 -*-
                                    ######################################
                                    ###   AR INTERCOM                  ###
                                    ###   VERSION : 1 Beta             ###
                                    ###   UPDATE  : 21-02-2021         ###
                                    ###   LICENCE : FREE               ###
                                    ###   DESIGNED AND EDITED BY       ###
                                    ###   ===== ANTARES MUGISHO ====== ###
                                    ###   COPYRIGHT 2021               ###
                                    ######################################

# ============================================== MAIN PROGRAM FILE =====================================================

from Serveur import Serveur



print("\n██████ AR INTERCOM Beta ██████\n Designed by a Creative Mind.\n"
      "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

server = Serveur()
server.create_socket_server()
server.launch_server()

# =========================================== ALL THANKS TO MY GOD =====================================================