from classi.carte import Mazzo
from classi.giocatore import Giocatore

class Banco(Giocatore):

    __mazzo = None

    def __init__(self,numero_carte):
        super().__init__('Banco', 1)
        self.__mazzo = Mazzo(numero_carte)

    def estrai(self):
        mazzo = self.__mazzo.get_Mazzo()
        return mazzo.pop(len(mazzo)-1)




