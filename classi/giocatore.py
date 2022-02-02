


class giocatore:
    __nome = ""
    __soldi = 0
    

    def __init__(self,nome,soldi):
        self.__nome = nome
        assert isinstance(soldi,int) > 0 , "non valido"
        self.__soldi = soldi
        self.__carte = []   # CARTE ESTRATTE

    def get_carte(self):
        return self.__carte

    def set_carte(self, carta):
        self.__carte.append(carta)

    def cont_carte(self):
        if sum(self.__carte) > 21:
            return "perso"
        elif(sum(self.__carte) == 21):
            return "bj"
        else:
            return 'contin'
