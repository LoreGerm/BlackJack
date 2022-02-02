from ast import Break
from classi.banco import banco


class giocatore:

    def __init__(self,nome,soldi):
        self.__nome = nome
        assert isinstance(soldi,int) > 0 , "non valido"
        self.__soldi = soldi
        self.__carte = []   # CARTE ESTRATTE
        self.__tot_carte = 0
        self.__scommessa = 0

    def get_carte(self):
        return self.__carte

    def set_carte(self, carta):
        self.__carte.append(carta)
        if carta.get_numero() == 'J' or carta.get_numero() == 'K' or carta.get_numero() == 'Q':
            self.__tot_carte += 10
        else:
            self.__tot_carte += carta.get_numero()

    def cont_carte(self):
        if sum(self.__carte) > 21:
            return "perso"
        elif(sum(self.__carte) == 21):
            return "bj"
        else:
            return 'contin'


    def get_totale(self):
        return self.__tot_carte

    def scommetti(self,scommessa):
        if scommessa < self.__soldi:
            self.__soldi -= scommessa
            self.__scommessa = scommessa
        else:
            return False


    def turno(self):
        while x != 3:
            print('1 - Chiedi carta')
            print('2 - Raddoppia')
            print('3 - Shtatt ferm')
            x = input("Scegli la mossa:  ")
            if x == 1:
                banco.distribuisci(self)
                # CONFRONTA TOTALE
            elif x == 2:
                raddoppio = self.__scommessa * 2
                self.__soldi -= self.__scommessa
                banco.distribuisci(self)
                # CONFRONTA TOTALE
                Break
