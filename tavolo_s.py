import zmq
import json


class Tavolo_s:

    def __init__(self,porta):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.bind("tcp://192.168.200.70:"+porta)


    def ricevi_comando(self):
        x = self.__socket.recv_json()
        dict = json.loads(x)
        print(dict)
        print('')
        return dict


    def mostra_menu(self):
        self.__socket.send_string('menu')
        scelta = int(self.__socket.recv_string())
        if scelta == 1:
            self.__socket.send_string('Stai fermo')
        elif scelta == 2:
            self.__socket.send_string('Carta')
        else:
            self.__socket.send_string('Raddoppia')

        print(scelta)



    def ricv_scomm(self):
        scomm = json.loads(self.__socket.recv_json())



    def partita(self):
        while True:
            x = self.ricevi_comando()
            if x['cmd'] == 'menu':
                self.mostra_menu()
            elif x['cmd'] == 'scomm':
                self.ricv_scomm()


'''
if __name__ == '__main__':
    t = Tavolo_s()
    while True:
        x = t.ricevi_comando()
        if x['cmd'] == 'menu':
            t.mostra_menu()
        elif x['cmd'] == 'scomm':
            t.ricv_scomm()
'''