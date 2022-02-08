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
    players.append(player)
    b = banco(13,players)







    

