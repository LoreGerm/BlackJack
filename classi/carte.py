from random import random
import random

class Mazzo:
    __mazzo_carte = []
    def __init__(self, numero_carte):
        for i in range (1,numero_carte + 1, 1):
            self.__mazzo_carte.append(Quadri(i))
            self.__mazzo_carte.append(Picche(i))
            self.__mazzo_carte.append(Cuori(i))
            self.__mazzo_carte.append(Fiori(i))

        random.shuffle(self.__mazzo_carte)

    def get_Mazzo(self):
        return self.__mazzo_carte

    def estrai(self):
        return self.__mazzo_carte.pop(len(self.__mazzo_carte)-1)

class Carta:
    __seme = ""
    __numero = 0

    def get_seme(self):
        return self.__seme

    def __str__(self):
        return str(self.numero) + " di " + self.seme


class Quadri(Carta):

    def __init__(self, numero):
        self.seme = "quadri"
        self.numero = numero
    
    

class Fiori(Carta):

    def __init__(self, numero):
        self.seme = "Fiori"
        self.numero = numero


class Picche(Carta):

    def __init__(self, numero):
        self.seme = "Picche"
        self.numero = numero


class Cuori(Carta):

    def __init__(self, numero):
        self.seme = "Cuori"
        self.numero = numero