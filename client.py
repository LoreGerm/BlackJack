import json
from pickle import UNICODE
import zmq

from classi.giocatore import giocatore


class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.200.70:5555")

    p = giocatore('jachille', 500000)
    x = json.dumps(p.__dict__)
    s = bytes(x, 'utf-8')
    socket.send(s)


    