
import time 
import zmq
import multiprocessing as mp

from classi.banco import Banco
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo

# CRIPTARE I DATI CON AES

class Server:

    __context = zmq.Context()
    __socket = __context.socket(zmq.REP)
    __socket.bind("tcp://192.168.1.159:5555")
    __b = Banco(13)
    __players = []
    __fine = False

    def tempo(self):
        n = 1
        a = time.time()
        b = a + 15
        while a < b:
            a = time.time()
            print(a)
        self.__fine = True
        
    def ricevi(self):
        for i in range(20):
            print('ciao')
        
    def __init__(self):
        
        t = mp.Process(target = self.tempo())
        t2 = mp.Process(target=self.ricevi())
        t.start()
        t2.start()
        
        t.join()
        t2.join()
        
        
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
        
'''
        
hgfugrfqugrfqgf
    
