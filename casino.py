from classi.giocatore import Giocatore
from classi.tavolo import Tavolo
import zmq
import json
import uuid

class Casino:
    __li_atts = []

    def __init__(self):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.bind("tcp://0.0.0.0:5555")

    def ricevi_comando(self):
        x = self.__socket.recv_json()
        dict = json.loads(x)
        print(dict)
        return dict

    def aggiungi_attesa(self, dict):
        dict['id'] = uuid.uuid4()
        dict['soldi'] = 50000
        self.__li_atts.append(Giocatore(dict['valore'], dict['soldi'], dict['id']))
        self.__socket.send_string('sei in attesa')
        print(self.__li_atts[0].__dict__)


    def crea_tavolo_1(self):
        if len(self.__li_atts) >= 1:
            gio = []
            gio.append(self.__li_atts.pop(0))
            t = Tavolo(gio, 8000)
            self.__socket.send_string('sei in tavolo1')

        print(t.__dict__)



if __name__ == '__main__':

    c = Casino()
    while True:
        x = c.ricevi_comando()
        if x['cmd'] == 'login':
            c.aggiungi_attesa(x)
        elif x['cmd'] == 'tv1':
            c.crea_tavolo_1()