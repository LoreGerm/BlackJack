from classi.banco import banco
from classi.giocatore import giocatore





p1 = giocatore('Ciatteo',50000)

player = [p1]

b = banco(13,player)

print('Soldi totali: ', p1.get_soldi())        
scommessa = int(input('Soldi da puntare: '))
p1.scommetti(scommessa)


b.distribuisci(player)



print(p1.get_nome(),': ', p1.str_carte(), 'totale: ',p1.get_totale())
print('---------------------------------')
print('Banco: ', b.get_carte()[1])
print('---------------------------------')

p1.turno_giocatore()

b.turno_banco()
print('carte bnco: ', b.str_carte(), 'totale: ',b.get_totale())

print(b.confronto())
print(p1.get_soldi())


# CREA LISTA GIOCAORI   OK
# CREA BANCO    OK

# :INIZIO GIOCO

# SCOMMETTI     OK
# DISTIBUISCI 2 CARTE   OK
# TURNO GIOCATORE E BANCO (CHIEDE CARTA(CHECK SBALLO O BJ), STARE, RADDOPPIO)   OK
# CONFRONTO CON BANCO   OK
# RISULTATO SCOMMESSA   OK

# GOTO INIZIO
