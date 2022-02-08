#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.200.70:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"'{'_giocatore__nome': 'jachille', '_giocatore__soldi': 500000, '_giocatore__carte': [], '_giocatore__tot_carte': 0, '_giocatore__scommessa': 0, '_giocatore__id': 139909014844368}'")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))