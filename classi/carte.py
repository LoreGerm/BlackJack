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


class Carta:
    __seme = ""
    __numero = 0

    def get_seme(self):
        return self.__seme

    def __repr__(self):
        return str(self.numero) + " di " + self.seme

    def get_numero(self):
        return self.numero


class Quadri(Carta):

    def __init__(self, numero):
        if numero == 11:
            self.seme = "Quadri"
            self.numero = 'J'
        elif numero == 12:
            self.seme = "Quadri"
            self.numero = 'Q'
        elif numero == 13:
            self.seme = "Quadri"
            self.numero = 'K'
        else:
            self.seme = "Quadri"
            self.numero = numero
    
    

class Fiori(Carta):

    def __init__(self, numero):
        if numero == 11:
            self.seme = "Fiori"
            self.numero = 'J'
        elif numero == 12:
            self.seme = "Fiori"
            self.numero = 'Q'
        elif numero == 13:
            self.seme = "Fiori"
            self.numero = 'K'
        else:
            self.seme = "Fiori"
            self.numero = numero


class Picche(Carta):

    def __init__(self, numero):
        if numero == 11:
            self.seme = "Picche"
            self.numero = 'J'
        elif numero == 12:
            self.seme = "Picche"
            self.numero = 'Q'
        elif numero == 13:
            self.seme = "Picche"
            self.numero = 'K'
        else:
            self.seme = "Picche"
            self.numero = numero


class Cuori(Carta):

    def __init__(self, numero):
        if numero == 11:
            self.seme = "Cuori"
            self.numero = 'J'
        elif numero == 12:
            self.seme = "Cuori"
            self.numero = 'Q'
        elif numero == 13:
            self.seme = "Cuori"
            self.numero = 'K'
        else:
            self.seme = "Cuori"
            self.numero = numero