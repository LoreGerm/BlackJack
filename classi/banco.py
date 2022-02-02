from classi.carte import Mazzo

class banco(Mazzo):
    __carte = [] # OBJ MAZZO.ESTRATTE


    def __init__(self,numero_carte):
        super().__init__(numero_carte)

    def set_carte(self,carte):
        self.__carte.append(carte)

    def cont_carte(self):
        if sum(self.__carte) > 21:
            return "perso"
        elif(sum(self.__carte) == 21):
            return "bj"
        else:
            return 'contin'