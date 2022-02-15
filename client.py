import json
import zmq

from classi.giocatore import Giocatore
class client:

    __context = zmq.Context()
    __socket = __context.socket(zmq.REQ)
    __socket.connect("tcp://192.168.1.8:5555")

    def crea_giocatore(self):
        self.__nome = input('Nome giocatore:  ')
        self.__socket.send_string(self.__nome)
        message = self.__socket.recv_string()
        print("Soldi: ", message)

    def scommetti(self):
        scommessa = input('Scommessa:  ')
        self.__socket.send_string(scommessa)
        message = self.__socket.recv_string()
        print('Soldi:  ', message-scommessa)

    def turno(self):
        message = self.__socket.recv_string()
        #print('Soldi:  ', message-scommessa)






    