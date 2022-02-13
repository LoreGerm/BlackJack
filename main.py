from classi.banco import Banco
from classi.giocatore import Giocatore
from classi.tavolo import Tavolo


p1 = Giocatore('Ciatteo', 50000)
p2 = Giocatore('Jachille', 50000)
p3 = Giocatore("Jack la trivella dell'adriatico", 50000)
player = [p1,p2,p3]
scom1 = p1.scommetti(40000)
scom2 = p2.scommetti(100)
scom3 = p3.scommetti(6990)

scommesse = [scom1,scom2,scom3]

b = Banco(13)
t = Tavolo(b, player)

t.turno_giocatore(scommesse)
t.turno_banco()

for i in range(len(player)-1):
    print(player[i].get_soldi())



'''
SPLIT : instanzia un'altro giocatore uguale, la vittoria va al primo giocatore
Array in giocatore per lo split con la seconda carta del giocatore
'''