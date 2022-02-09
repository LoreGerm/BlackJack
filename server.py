import json
import zmq

from classi.banco import banco
from classi.giocatore import giocatore

class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")


    def byte_to_str(a):
        x = str(a, 'utf-8')
        x = json.loads(a)
        return x

    

    while True:
        players = []
        player = socket.recv()  # SERVER RICEVE I GIOCATORI DAL CLIENT
        player = byte_to_str(player)
        players.append(player)
        socket.send(b"a")
        print(players)

        #b = banco(13,players)

    





    

