from classi.giocatore import giocatore


class tavolo:
    __giocatore = [] # OBJ GIOCATORE
    __banco = [] # OBJ BANCO
    __mazzo = [] # OBJ MAZZO

    def __init__(self,giocatore, banco, mazzo):
        self.__mazzo = mazzo
        self.__banco = banco
        self.__giocatore = giocatore

    def distribuisci_giocatore(self):
        self.__giocatore.set_carte(self.__banco.estrai())

    def distribuisci_banco(self):
        self.__banco.set_carte(self.__banco.estrai())

    def confronto(self):
        if self.__giocatore.cont_carte() == "contin" and self.__banco.cont_carte() == "contin":
            if self.__giocatore.cont_carte() > self.__banco.cont_carte():
                return "vinto"
            elif(self.__giocatore.cont_carte() == self.__banco.cont_carte()):
                return "pari"
            else:
                return "perso"
        elif(self.__giocatore.cont_carte() == "bj" and self.__banco.cont_carte() == "contin"):
            return "vinto"
        elif(self.__banco.cont_carte() == "bj" and self.__giocatore.cont_carte() == "contin"):
            return 'perso'
        elif(self.__banco.cont_carte() == "perso" and self.__banco.cont_carte() == "contin" or  self.__banco.cont_carte() == "bj"):
            return "perso"
        else:
            return "vinto"
    