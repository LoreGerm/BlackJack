import json
import zmq

from classi.giocatore import Giocatore
class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.1.159:5555")




    nome = input('Nome giocatore:  ')
    p = Giocatore(nome, 500000)
    p_json = json.dumps(p.__dict__)
    socket.send_json(p_json)
    message = socket.recv_json()
    print("Soldi: ", message)

    socket.close()




    