
import time 
import zmq
import threading as tr

from classi.banco import Banco
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo

# CRIPTARE I DATI CON AES

class Server:

    __context = zmq.Context()
    __socket = __context.socket(zmq.REP)
    __socket.bind("tcp://0.0.0.0:5555")
    __socket.RCVTIMEO = 10000
    __b = Banco(13)
    __giocatori = []
    __fine = False
    __scommesse_tot = []
    __socket.g

    def crea_giocatore(self):
        while self.__fine == False:
            try:
                x = self.__socket.recv_string()  # SERVER RICEVE I GIOCATORI DAL CLIENT
                player = Giocatore(x, 50000)
                soldi = str(player.get_soldi())
                self.__socket.send_string(soldi)
                self.__giocatori.append(player)
            except:
                self.__fine = True

    def scommessa(self):
        while self.__fine == False:
            try:
                for i in self.__giocatori:
                    scommessa = self.__socket.recv_string()
                    self.__scommesse_tot.append(scommessa)
                    soldi = str(i.get_soldi())
                    self.__socket.send_string(soldi)
            except:
                for i in range (len(self.__giocatori)-1):
                    self.__t.set_scommessa(self.__giocatori[i],self.__scommesse_tot[i])
                self.__fine = True

    def chiedi_mossa(self):
        while self.__fine == False:
            try:
                self.__t.turno_giocatore()
            except:
                self.__fine = True

    def rcv_ping(self):
        nome = self.__socket.recv_string()
        self.__socket.send_string('0')
        print(nome)
        


    def __init__(self):
        self.crea_giocatore()
        self.rcv_ping()
        ping = self.__socket.recv_string()
        print(ping)
        #self.crea_giocatore()
        #self.__t = Tavolo(self.__b, self.__giocatori)
        #print(self.__giocatori)
    
        
if __name__ == "__main__":
    s = Server()

    
# PER SOMMESSE E TURNO (PING)
# IL CLIENT MANDA PER 10 SECONDI IL SUO NOME(PING) AL SERVER 
# IL SERVER RICEVE I NOMI E LI CONFRONTA CON I GIOCATORI IN ORDINE
# FINO A QUANDO NON TROVA LA CORRISPONDENZA A CUI MANDARE IL TURNO

