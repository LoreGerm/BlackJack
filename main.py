
from classi.banco import banco
from classi.carte import *
from classi.giocatore import giocatore





p1 = giocatore('Ciatteo',50000)
p2 = giocatore('Leonzio',10000000)

player = [p1,p2]

b = banco(13,player)

p1.scommetti(100)

b.distribuisci(player)
b.distribuisci(player)

print(str(p1.get_carte()[0]),str(p1.get_carte()[1]))
print('--------------------------------')
print(str(p2.get_carte()[0]),str(p2.get_carte()[1]))
print('--------------------------------')
print(str(b.get_carte()[0]),str(b.get_carte()[1]))
print('---------------------------------')

print(p1.turno())


# CREA LISTA GIOCAORI   OK
# CREA BANCO    OK

# :INIZIO GIOCO

# SCOMMETTI     OK
# DISTIBUISCI 2 CARTE   OK
# TURNO GIOCATORE (CHIEDE CARTA(CHECK SBALLO O BJ), STARE, RADDOPPIO)
# CONFRONTO CON BANCO
# RISULTATO SCOMMESSA

# GOTO INIZIO
