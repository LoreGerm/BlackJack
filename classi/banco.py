from classi.carte import Mazzo

class banco(Mazzo):
    __carte = [] # CARTE ESTRATTE
    __giocatori = [] # OBJ GIOCATORE


    def __init__(self,numero_carte,giocatori):
        super().__init__(numero_carte)
        self.__giocatori = giocatori    # PASSARE TUTTI I GIOCATORI (NON CONSIDERARE IL BANCO)
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
        else:
            giocatori.set_carte(cls.estrai())

    def turno_banco(self):
        x = 0
        while x != 3:
            if self.__tot_carte < 17:
                print('1 - Shtatt ferm')
                print('2 - Chiedi carta')
                x = input("Scegli la mossa:  ")
            else:
                break
            


