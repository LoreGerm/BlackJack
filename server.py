import json
import zmq

from classi.banco import banco
from classi.giocatore import giocatore

class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")
    message = ""

    players = []
    player = socket.recv()  # SERVER RICEVE I GIOCATORI DAL CLIENT
    player = str(player, 'utf-8')
    player = json.loads(player)
    players.append(player)
    print(players)

    #b = banco(13,players)







    

