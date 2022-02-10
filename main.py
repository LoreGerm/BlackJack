from classi.banco import Banco
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo


p1 = Giocatore('Ciatteo', 50000)
player = [p1]
b = Banco(13)
t = Tavolo(b, player)
print(p1.get_id())
t.set_carte(player)
print(t.get_carte())




# ESTRAI  OK
#


# :INIZIO GIOCO

# SCOMMETTI     OK
# DISTIBUISCI 2 CARTE   OK
# TURNO GIOCATORE E BANCO (CHIEDE CARTA(CHECK SBALLO O BJ), STARE, RADDOPPIO)   OK
# CONFRONTO CON BANCO   OK
# RISULTATO SCOMMESSA   OK

# GOTO INIZIO
