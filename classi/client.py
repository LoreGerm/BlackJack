import zmq


class client:

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.200.70:5555")

    #  Do 10 requests, waiting each time for a response
    for request in range(10):
        print("Sending request %s …" % request)
        socket.send(b"ciao")

        #  Get the reply.
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request, message))