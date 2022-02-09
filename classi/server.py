import zmq


class server:

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.200.70:5555")
    message = ""


    
    while True:
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message}")

        #  Do some 'work'


        #  Send reply back to client
        socket.send(b"a")