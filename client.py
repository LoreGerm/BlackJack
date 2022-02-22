from classi.giocatore import Giocatore
import zmq
import json

class Client:

    context = zmq.Context()
    __socket = context.socket(zmq.REQ)
    __socket.connect("tcp://0.0.0.0:5555")

    def connetti_casino(self):
        self.__nome = input('Nome giocatore:  ')
        dict = {
            'cmd' : 'login',
            'valore' : self.__nome,
            'id' : 0
        }
        p_json = json.dumps(dict)
        self.__socket.send_json(p_json)
        message = self.__socket.recv_string()
        print(message)

    def connetti_tavolo1(self):
        dict = {
            'cmd' : 'tv1',
            'valore' : self.__nome,
            'id' : 0
        }
        p_json = json.dumps(dict)
        self.__socket.send_json(p_json)
        message = self.__socket.recv_string()
        print(message)


    def richiedi_menu(self):
        dict = {
            'cmd' : 'menu',
            'valore' : self.__nome,
            'id' : 0
        }
        p_json = json.dumps(dict)
        self.__socket.send_json(p_json)
        mesg = self.__socket.recv_string()
        if mesg == 'menu':
            self.__socket.send_string(Giocatore.scelta())


    


if __name__ == '__main__':
    c = Client()
    c.connetti_casino()
    c.connetti_tavolo1()
    c.richiedi_menu()