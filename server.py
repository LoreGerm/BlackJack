import json
import zmq

from classi.banco import Banco
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo

# CRIPTARE I DATI CON AES

class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")
    b = Banco(13)
    players = []

    

    while True:
        
        p = socket.recv_string()  # SERVER RICEVE I GIOCATORI DAL CLIENT
        player = Giocatore(p,50000)
        soldi = str(player.get_soldi())
        players.append(player)
        socket.send_string(soldi)
        t = Tavolo(b, players)
        print(players)
        

        #b = banco(13,players)


    
