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
        self.__t1_0 = Tavolo([],8000)
        self.__t1_1 = Tavolo([],8001)
        self.__t1_2 = Tavolo([],8002)
        self.__lista_t1 = [self.__t1_0, self.__t1_1, self.__t1_2]

    def ricevi_comando(self):
        x = self.__socket.recv_json()
        dict = json.loads(x)
        print(dict)
        print('')
        return dict

    def aggiungi_attesa(self, dict):
        dict['id'] = uuid.uuid4()
        dict['soldi'] = 50000
        self.__li_atts.append(Giocatore(dict['valore'], dict['soldi'], dict['id']))
        self.__socket.send_string('sei in attesa')
        print(self.__li_atts[0].__dict__)
        print('')


    def crea_tavolo_1(self):
        for i in self.__lista_t1:
            if len(i.get_giocatori()) == 1:
                if len(self.__li_atts) >= 1:
                    gio = []
                    gio.append(self.__li_atts.pop(0))
                    i.set_giocatore(gio)
                    self.__socket.send_string('sei in tavolo:  ', i.get_id())
                    break
                    #################### return i ########################## RITORNA IL TAVOLO UTILIZZATO

        print(i.__dict__)
        print('')

    # PROVA
    def gioca(self, tavolo):
        tavolo.turno_giocatore()
        tavolo.turno_banco()


if __name__ == '__main__':

    c = Casino()
    while True:
        x = c.ricevi_comando()
        if x['cmd'] == 'login':
            c.aggiungi_attesa(x)
        elif x['cmd'] == 'tv1':
            c.crea_tavolo_1()
            #c.gioca(c.crea_tavolo_1())