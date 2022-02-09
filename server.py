import json
import zmq

from classi.banco import banco
from classi.giocatore import giocatore
from classi.utility import utility

class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")



    

    while True:
        players = []
        player = socket.recv()  # SERVER RICEVE I GIOCATORI DAL CLIENT
        player = utility.byte_to_str(player)
        soldi = player['_giocatore__soldi']
        soldi = utility.str_to_byte(soldi)
        players.append(player)
        socket.send(soldi)
        print(players)
        

        #b = banco(13,players)

    





    

