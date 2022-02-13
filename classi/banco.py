from classi.carte import Mazzo

class Banco(Mazzo):

    def __init__(self,numero_carte):
        super().__init__(numero_carte)
        self.__id = id(self)

    def get_id(self):
        return self.__id

    def estrai(self):
        mazzo = super().get_Mazzo()
        return mazzo.pop(len(mazzo)-1)

"""
    def confronto(self):
        for i in range(len(self.__giocatori)-1):
            if self.__tot_carte > 21:
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__giocatori[i].get_scommessa()*2)
                return 'vinto'
            elif self.__giocatori[i].get_totale() > 21 or self.__tot_carte > self.__giocatori[i].get_totale():
                return 'perso'
            elif self.__tot_carte == self.__giocatori[i].get_totale():
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__giocatori[i].get_scommessa())
                return 'pari'
            elif self.__tot_carte < self.__giocatori[i].get_totale():
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__giocatori[i].get_scommessa()*2)
                return 'vinto'
            elif self.__tot_carte == 21 and len(self.__carte) == 2 and len(self.__giocatori[i].get_carte()) > 2:
                return 'perso'
            else:
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__giocatori[i].get_scommessa()*2)
                return 'vinto'
"""


