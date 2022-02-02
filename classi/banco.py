from classi.carte import Mazzo

class banco(Mazzo):
    __carte = [] # CARTE ESTRATTE
    __giocatori = [] # OBJ GIOCATORE


    def __init__(self,numero_carte,giocatori):
        super().__init__(numero_carte)
        self.__giocatori = giocatori    # PASSARE TUTTI I GIOCATORI (NON CONSIDERARE IL BANCO)

    def set_carte(self,carte):
        self.__carte.append(carte)

    def cont_carte(self):
        if sum(self.__carte) > 21:
            return "perso"
        elif(sum(self.__carte) == 21):
            return "bj"
        else:
            return 'contin'

    def distribuisci(self,giocatori):
        for i in giocatori:
            i.set_carte(self.estrai())
