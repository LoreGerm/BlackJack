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




