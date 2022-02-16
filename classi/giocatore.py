


class Giocatore:


    def __init__(self,nome,soldi):
        self.__nome = nome
        assert isinstance(soldi,int) > 0 , "non valido"
        self.__soldi = soldi
        self.__id = id(self)
        self.__perso = False
        self.__cont = 0

    def scelta(self):
        print('1 - Shtatt ferm')
        print('2 - Chiedi carta')
        if self.__cont == 0:
            print('3 - Raddoppia')
        self.__cont = 1
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

