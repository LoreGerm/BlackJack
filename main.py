
from classi.banco import banco
from classi.carte import *
from classi.giocatore import giocatore





p1 = giocatore('Ciatteo',50000)
p2 = giocatore('Leonzio',10000000)

player = [p1,p2]

b = banco(13,player)

b.distribuisci(player)

print(str(p1.get_carte()[0]))
print('--------------------------------')
print(str(p2.get_carte()[0]))
print('--------------------------------')
print(str(b.get_carte()[0]))


