
import time
import zmq

class Client:

    __context = zmq.Context()
    __socket = __context.socket(zmq.REQ)
    __socket.connect("tcp://192.168.200.70:5555")

    def crea_giocatore(self):
        self.__nome = input('Nome giocatore:  ')
        self.__socket.send_string(self.__nome)
        message = self.__socket.recv_string() #printa soldi
        print("Soldi: ", message)

    def scommetti(self):
        scommessa = input('Scommessa:  ')
        self.__socket.send_string(scommessa)
        message = self.__socket.recv_string()
        print('Soldi:  ', message-scommessa)

    def turno(self):
        message = self.__socket.recv_string()
#        print('Soldi:  ', message-scommessa)

# da 18 a 26

    def ping(self):
        pass


    def __init__(self):
        self.crea_giocatore()
        self.ping()



if __name__ == '__main__':

    c = Client()

    