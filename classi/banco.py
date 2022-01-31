from classi.carte import Mazzo

class banco:
    __carte = [] # OBJ MAZZO.ESTRATTE

    def estrai(self):
        return Mazzo.estrai()

    def set_carte(self,carte):
        self.__carte.append(carte)

    def cont_carte(self):
        if sum(self.__carte) > 21:
            return "perso"
        elif(sum(self.__carte) == 21):
            return "bj"
        else:
            return 'contin'