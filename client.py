
import json
import time
import zmq

class Client:

    __context = zmq.Context()
    __socket = __context.socket(zmq.REQ)
    __socket.connect("tcp://192.168.200.70:5555")


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


    def ping(self):
        self.__socket.RCVTIMEO = 1000
        x = False
        self.__socket.send_string("self.__nome")
        while x == False:
            try:
                message = self.__socket.recv_string()
                self.__socket.send_string("sono io")
                print(message)
                x = True
            except Exception as e:
                print('messaggio non ricevuto')
                print(e)


    def __init__(self):
        self.crea_giocatore()
        self.ping()



if __name__ == '__main__':

    c = Client()

    