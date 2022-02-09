import json
import zmq

from classi.giocatore import giocatore
class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.200.70:5555")




    nome = input('Nome giocatore:  ')
    p = giocatore(nome, 500000)
    p_json = json.dumps(p.__dict__)
    socket.send_json(p_json)
    message = socket.recv_json()
    print("Soldi: ", message)

    socket.close()




    