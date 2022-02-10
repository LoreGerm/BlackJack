# dizionario con chiave id giocatore e valore lista carte

class Tavolo:


    def __init__(self, banco, giocatori):
        self.__scommesse = {}
        self.__giocatori = giocatori
        self.__giocatori.append(banco)  # GIOCATORI + BANCO
        self.__banco = banco
        self.__carte_totali = {}

    def get_carte_giocatore(self,giocatore):
        return self.__carte_totali[giocatore.get_id()]
    
    def get_tot_carte_giocatore(self,giocatore):
        x = 0
        for i in self.get_carte_giocatore(giocatore):
            if i.get_numero() == 'J' or i.get_numero() == 'K' or i.get_numero() == 'Q':
                x += 10
            elif i.get_numero() == 'A':
                x += 11
            else:
                x += i.get_numero()
        if x > 21:
            for i in self.get_carte_giocatore(giocatore):
                if i.get_numero() == 'A':
                    x -= 10
        return x

    def get_carte(self):
        return self.__carte_totali

    def get_scommesse(self):
        return self.__scommesse

    def confronto(self):
        pass


    def set_scommessa(self, giocatore, scommessa):
        self.__scommesse[giocatore.get_id()] = scommessa




    def set_carte(self, giocatori):
        if isinstance(giocatori, list):
            for i in giocatori:
                if i.get_id() in self.__carte_totali:
                    self.__carte_totali[i.get_id()].append(self.__banco.estrai())
                else:
                    self.__carte_totali[i.get_id()] = [self.__banco.estrai()]
        else:
            if giocatori.get_id() in self.__carte_totali:
                self.__carte_totali[giocatori.get_id()].append(self.__banco.estrai())
            else:
                self.__carte_totali[giocatori.get_id()] = [self.__banco.estrai()]




    def turno_giocatore(self,scommessa):
        for i in range (len(self.__giocatori)-1):
            self.set_scommessa(self.__giocatori[i],scommessa[i]) # SCOMMETTE

        for i in range (len(self.__giocatori)):
            self.set_carte(self.__giocatori[i])   # PRIME CARTE
        for i in range (len(self.__giocatori)):
            self.set_carte(self.__giocatori[i])   # SECONDE CARTE
        
        print(self.__carte_totali, '\n')

        for i in range (len(self.__giocatori)-1):
            bj = 0
            print('\n',self.__giocatori[i].get_nome())  # NOME GIOCATORE
            print(self.__carte_totali[self.__giocatori[i].get_id()])    # CARTE GIOCATORE
            print('Totale: ',self.get_tot_carte_giocatore(self.__giocatori[i])) # TOTALE CARTE GIOCATORE
            if self.get_tot_carte_giocatore(self.__giocatori[i]) == 21:
                print('21 vittoria grande baldoria')
                bj = 1
            if bj == 0:
                x = self.__giocatori[i].scelta()
                while x != 1:
                    if x == 2:
                        self.set_carte(self.__giocatori[i])     # ASSEGNA CARTE
                        print(self.__carte_totali[self.__giocatori[i].get_id()])    # CARTE GIOCATORE
                        print('Totale: ',self.get_tot_carte_giocatore(self.__giocatori[i])) # TOTALE CARTE GIOCATORE
                        if self.get_tot_carte_giocatore(self.__giocatori[i]) > 21:
                            print('Sballato')
                            break
                        elif self.get_tot_carte_giocatore(self.__giocatori[i]) == 21:
                            print('21')
                            break
                        else:
                            x = self.__giocatori[i].scelta()
            

        
            

