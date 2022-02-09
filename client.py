import json
import zmq

from classi.giocatore import giocatore

class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.200.70:5555")



    def obj_to_byte(obj):
        obj_json = json.dumps(obj.__dict__)
        obj_byte = bytes(obj_json, 'utf-8')
        return obj_byte



    nome = input('Nome giocatore:  ')
    p = giocatore(nome, 500000)
    p_byte = obj_to_byte(p)
    socket.send(p_byte)
    message = socket.recv()
    print("Received reply ", message)




    