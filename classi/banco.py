from classi.carte import Mazzo

class banco(Mazzo):
    __carte = [] # CARTE ESTRATTE
    __giocatori = [] # OBJ GIOCATORE


    def __init__(self,numero_carte,giocatori):
        super().__init__(numero_carte)
        self.__giocatori = giocatori   
        self.__giocatori.append(self)
        self.__tot_carte = 0

    def get_totale(self):
        return self.__tot_carte

    def set_carte(self,carta):
        self.__carte.append(carta)
        if carta.get_numero() == 'J' or carta.get_numero() == 'K' or carta.get_numero() == 'Q':
            self.__tot_carte += 10
        else:
            self.__tot_carte += carta.get_numero()
        if self.__tot_carte > 21:
            for i in self.__carte:
                if i.get_numero() == 1:
                    self.__tot_carte -= 10

    def str_carte(self):
        carte = []
        if isinstance(self.get_carte(),list):
            for i in self.get_carte():
                carte.append(str(i))
            return carte
        else:
            return str(self.get_carte())

    def get_carte(self):
        return self.__carte

    def cont_carte(self):
        if sum(self.__carte) > 21:
            return "perso"
        elif(sum(self.__carte) == 21):
            return "bj"
        else:
            return 'contin'

    @classmethod
    def distribuisci(cls,giocatori):
        if isinstance(giocatori,list):
            for i in giocatori:
                i.set_carte(cls.estrai())
                i.set_carte(cls.estrai())
        else:
            giocatori.set_carte(cls.estrai())


    def turno_banco(self):
        bool = False
        for i in range(len(self.__giocatori)-1):
            if self.__giocatori[i].get_totale() > 21:
                bool = True
            else:
                bool = False
        if bool == False:
            while self.__tot_carte < 17:
                self.distribuisci(self)


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



