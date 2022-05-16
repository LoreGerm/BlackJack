from classi.carte import Mazzo
from classi.giocatore import Giocatore

class Banco(Giocatore):

    __mazzo = None

    def __init__(self,numero_carte):
        __mazzo = Mazzo(numero_carte)
        super.__init__('Banco', 0)

    def estrai(self):
        mazzo = super().get_Mazzo()
        return mazzo.pop(len(mazzo)-1)




