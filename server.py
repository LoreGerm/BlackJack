
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
    __socket.RCVTIMEO = 10000
    __b = Banco(13)
    __players = []
    __fine = False

    def ricevi(self):
        while self.__fine == False:
            try:
                x = self.__socket.recv_string()  # SERVER RICEVE I GIOCATORI DAL CLIENT
                print(x)
                player = Giocatore(x, 50000)
                soldi = str(player.get_soldi())
                self.__players.append(player)
                self.__socket.send_string(soldi)
            except:
                self.__fine = True



    def __init__(self):
        self.ricevi()
        t = Tavolo(self.__b, self.__players)
        print(self.__players)
    
        
if __name__ == "__main__":
    s = Server()
    

'''
    def tempo(self):
        a = time.time()
        b = a + 5
        while a < b:
            a = time.time()
        self.__fine = True
        print("Chiudo il server")
        self.__socket.close()

    t = mp.Thread(target = self.tempo)
    t.start()
'''

    

