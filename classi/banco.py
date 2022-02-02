from classi.carte import Mazzo

class banco(Mazzo):
    __carte = [] # CARTE ESTRATTE
    __giocatori = [] # OBJ GIOCATORE


    def __init__(self,numero_carte,giocatori):
        super().__init__(numero_carte)
        self.__giocatori = giocatori    # PASSARE TUTTI I GIOCATORI (NON CONSIDERARE IL BANCO)
        self.__giocatori.append(self)

    def set_carte(self,carte):
        self.__carte.append(carte)

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
        for i in giocatori:
            i.set_carte(cls.estrai())


