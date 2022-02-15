import json
import zmq

from classi.giocatore import Giocatore
class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.1.8:5555")




    nome = input('Nome giocatore:  ')
    socket.send_string(nome)
    message = socket.recv_string()
    print("Soldi: ", message)

    socket.close()




    