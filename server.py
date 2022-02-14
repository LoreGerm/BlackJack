import json
import zmq

from classi.banco import Banco
from classi.giocatore import Giocatore

class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")



    

    while True:
        players = []
        player = socket.recv_json()  # SERVER RICEVE I GIOCATORI DAL CLIENT
        player = json.loads(player)
        soldi = player['_Giocatore__soldi']
        players.append(player)
        socket.send_json(soldi)
        print(players)
        

        #b = banco(13,players)

    





    

