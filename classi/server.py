import zmq

from classi.banco import banco
from classi.giocatore import giocatore

class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")
    message = ""
    __p1 = giocatore('Ciatteo',50000)


    def scommetti(self):
        print('Soldi totali: ', self.__p1.get_soldi())        
        self.__scommessa = int(input('Soldi da puntare: '))
        self.__p1.scommetti(self.__scommessa)



    while True:
        #  Wait for next request from client

        

        message = socket.recv()

        self.__p1.turno_giocatore(message)

        socket.send()

        #  Do some 'work'

