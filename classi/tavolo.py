


'''
asso = Picche(1)
p1.set_carte(asso)



def set_carte(self, carta):
        self.__carte.append(carta)
        if carta.get_numero() == 1:
            self.__tot_carte += 11
        elif carta.get_numero() == 'J' or carta.get_numero() == 'K' or carta.get_numero() == 'Q':
            self.__tot_carte += 10
        else:
            self.__tot_carte += carta.get_numero()
        if self.__tot_carte > 21:
            for i in self.__carte:
                if i.get_numero() == 1:
                    self.__tot_carte -= 10



    #  Do 10 requests, waiting each time for a response
    for request in range(10):
        print("Sending request %s …" % request)
        socket.send(b"ciao")

        #  Get the reply.
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request, message))










    while True:
        #  Wait for next request from client

        

        message = socket.recv()

        

        socket.send()

        #  Do some 'work'
'''