
from classi.banco import Banco
from classi.tavolo import Tavolo

class Giocatore:


    def __init__(self,nome,soldi):
        self.__nome = nome
        assert isinstance(soldi,int) > 0 , "non valido"
        self.__soldi = soldi
        self.__id = id(self)
        self.__perso = False

    def scelta(self):
        print('1 - Shtatt ferm')
        print('2 - Chiedi carta')
        print('3 - Raddoppia')
        return int(input('Scegli mossa:  '))

    def get_perso(self):
        return self.__perso

    def get_soldi(self):
        return self.__soldi

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def set_perso(self,x):
        assert isinstance(x,bool), 'Valore non valido'
        self.__perso = x

    def set_nome(self, nome):
        self.__nome = nome

    def set_soldi(self, soldi):
        self.__soldi = soldi

    def scommetti(self,scommessa):
        if scommessa <= self.__soldi:
            self.__soldi -= scommessa
            return scommessa
        else:
            return False

    def turno_giocatore(self):
        cont = 0

        while True:
            pass

"""
        while x != 3:
            print('1 - Shtatt ferm')
            print('2 - Chiedi carta')
            if cont == 0:
                print('3 - Raddoppia')

            if x == '2':
                pass
            elif x == '3' and cont == 0:
                pass

            cont+=1




            def set_carte(self, carta):
                self.__carte.append(carta)
                if carta.get_numero() == 'J' or carta.get_numero() == 'K' or carta.get_numero() == 'Q':
                    self.__tot_carte += 10
                else:
                    self.__tot_carte += carta.get_numero()
                if self.__tot_carte > 21:
                    for i in self.__carte:
                        if i.get_numero() == 1:
                            self.__tot_carte -= 10
"""