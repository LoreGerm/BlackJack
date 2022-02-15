
import time 
import zmq
import threading as mp

from classi.banco import Banco
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo

# CRIPTARE I DATI CON AES

class Server:

    __context = zmq.Context()
    __socket = __context.socket(zmq.REP)
    __socket.bind("tcp://192.168.1.8:5555")
    __b = Banco(13)
    __players = []

    def tempo(self):
        global fine
        a = time.time()
        b = a + 10
        while a < b:
            a = time.time()
        fine = True
        
    def ricevi(self):
        while fine == False:
            p = self.__socket.recv_string()  # SERVER RICEVE I GIOCATORI DAL CLIENT
            player = Giocatore(p, 50000)
            soldi = str(player.get_soldi())
            self.__players.append(player)
            self.__socket.send_string(soldi)


    def __init__(self):
        
        t = mp.Thread(target = self.tempo)
        t.start()
        fine = False
        self.ricevi()
        t = Tavolo(self.__b, self.__players)
        print(self.__players)
    
        
if __name__ == "__main__":
    s = Server()
    
'''
    while self.__fine == False:
            p = self.__socket.recv_string()  # SERVER RICEVE I GIOCATORI DAL CLIENT
            player = Giocatore(p, 50000)
            soldi = str(player.get_soldi())
            self.__players.append(player)
            self.__socket.send_string(soldi)
            time.sleep(1)
'''

    

