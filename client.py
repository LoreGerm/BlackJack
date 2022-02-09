import json
import zmq

from classi.giocatore import giocatore
from classi.utility import utility

class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.200.70:5555")




    nome = input('Nome giocatore:  ')
    p = giocatore(nome, 500000)
    p_byte = utility.str_to_byte(p.__dict__)
    socket.send(p_byte)
    message = socket.recv()
    message = utility.byte_to_str(message)
    print("Soldi: ", message)

    socket.close()




    