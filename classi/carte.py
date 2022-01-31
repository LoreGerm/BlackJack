from random import random
import random

class Mazzo:
    mazzo_carte = []
    def __init__(self, numero_carte):
        for i in range (1,numero_carte + 1, 1):
            self.mazzo_carte.append(Quadri(i))
            self.mazzo_carte.append(Picche(i))
            self.mazzo_carte.append(Cuori(i))
            self.mazzo_carte.append(Fiori(i))

    def get_Mazzo(self):
        return self.mazzo_carte

    @classmethod
    def estrai(self):
        l_mazzo = len(self.mazzo_carte) - 1
        l_inizio = 0
        random.shuffle(self.mazzo_carte)
        num_estratto = random.randint(l_inizio, l_mazzo)
        return self.mazzo_carte.pop(num_estratto)

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