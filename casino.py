
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo
import zmq
import json
import uuid
import threading
from tavolo_s import Tavolo_s


class Casino:
    __li_atts = []

    def __init__(self):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.bind("tcp://192.168.200.70:5555")
        self.__t1_0 = Tavolo([],'8000')
        self.__t1_1 = Tavolo([],'8001')
        self.__t1_2 = Tavolo([],'8002')
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


    def agg_a_tavolo_1(self):
        for i in self.__lista_t1:
            if len(i.get_giocatori()) == 1:
                if len(self.__li_atts) >= 1:
                    gio = []
                    gio.append(self.__li_atts.pop(0))
                    i.set_giocatore(gio)
                    self.__socket.send_string(i.get_porta())
                    porta = i.get_porta()
                    break
        
        t = Tavolo_s(porta)
        th = threading.Thread(target=t.partita, args=()) ## THREAD DEL TAVOLO
        th.start()
        
        print(i.__dict__)
        print('')

##############################################################

    def tavolo(self,socket):
        x = self.ricevi_comando(socket)
        if x['cmd'] == 'menu':
            self.mostra_menu(socket)
        elif x['cmd'] == 'scomm':
            self.ricv_scomm(socket)



    def mostra_menu(self, socket):
        socket.send_string('menu')
        scelta = int(socket.recv_string())
        if scelta == 1:
            socket.send_string('Stai fermo')
        elif scelta == 2:
            socket.send_string('Carta')
        else:
            socket.send_string('Raddoppia')

        print(scelta)


    def ricv_scomm(self,socket):
        scomm = json.loads(socket.recv_json())
        
        



if __name__ == '__main__':

    c = Casino()
    while True:
        x = c.ricevi_comando()
        print(x)
        if x['cmd'] == 'login':
            c.aggiungi_attesa(x)
        elif x['cmd'] == 'tv1':
            c.agg_a_tavolo_1()
        
'''
        elif x['cmd'] == 'menu':
            c.mostra_menu()
        elif x['cmd'] == 'scomm':
            c.ricv_scomm()
'''
        