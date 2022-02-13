# dizionario con chiave id giocatore e valore lista carte



class Tavolo:


    def __init__(self, banco, giocatori):
        self.__scommesse = {}
        self.__giocatori = giocatori
        self.__giocatori.append(banco)  # GIOCATORI + BANCO
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
                    self.__carte_totali[i.get_id()].append(self.__giocatori[-1].estrai())
                else:
                    self.__carte_totali[i.get_id()] = [self.__giocatori[-1].estrai()]
        else:
            if giocatori.get_id() in self.__carte_totali:
                self.__carte_totali[giocatori.get_id()].append(self.__giocatori[-1].estrai())
            else:
                self.__carte_totali[giocatori.get_id()] = [self.__giocatori[-1].estrai()]




    def turno_giocatore(self,scommessa):
        for i in range (len(self.__giocatori)-1):
            self.set_scommessa(self.__giocatori[i],scommessa[i]) # SCOMMETTE

        for i in range (len(self.__giocatori)):
            self.set_carte(self.__giocatori[i])   # PRIME CARTE
        for i in range (len(self.__giocatori)):
            self.set_carte(self.__giocatori[i])   # SECONDE CARTE

        for i in self.__carte_totali:
            if self.__giocatori[-1].get_id() == i:
                print(i,' : ',self.__carte_totali[i],'\n')
            else:
                print(i,' : ',self.__carte_totali[i],' : ', self.__scommesse[i],'\n')
        

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
                            self.__giocatori[i].set_perso(True)
                            break
                        elif self.get_tot_carte_giocatore(self.__giocatori[i]) == 21:
                            print('21')
                            self.__giocatori[i].set_perso(False)
                            break
                        else:
                            x = self.__giocatori[i].scelta()
                    elif x==3:
                        scom = self.__giocatori[i].scommetti(self.__scommesse[self.__giocatori[i].get_id()])
                        if scom != False:
                            self.__scommesse[self.__giocatori[i].get_id()] *= 2
                            print(self.__scommesse[self.__giocatori[i].get_id()])
                            self.set_carte(self.__giocatori[i])     # ASSEGNA CARTE
                            print(self.__carte_totali[self.__giocatori[i].get_id()])    # CARTE GIOCATORE
                            print('Totale: ',self.get_tot_carte_giocatore(self.__giocatori[i])) # TOTALE CARTE GIOCATORE
                            if self.get_tot_carte_giocatore(self.__giocatori[i]) > 21:
                                print('Sballato')
                                self.__giocatori[i].set_perso(True)
                                break
                            elif self.get_tot_carte_giocatore(self.__giocatori[i]) == 21: 
                                print('21')
                                self.__giocatori[i].set_perso(False)
                                break
                            x = 1
                        else:
                            print('Saldo non sufficiente') #HAI MENO DEL DOPPIO DELLA PUNTATA
                            x = self.__giocatori[i].scelta()


    def turno_banco(self):
        print('\n')
        for i in self.__carte_totali:
            if self.__giocatori[-1].get_id() == i:
                print(i,' : ',self.__carte_totali[i],'\n')
            else:
                print(i,' : ',self.__carte_totali[i],' : ', self.__scommesse[i],'\n')

        while self.get_tot_carte_giocatore(self.__giocatori[-1]) < 17: # FIN TANTO CHE CARTE BANCO < 17
            s_vinti = 0
            s_persi = 0
            for i in range (len(self.__giocatori)-1): # CONTROLLA SE IL BANCO STA A PERDERE O VINCERE
                if self.__giocatori[i].get_perso() == True or self.get_tot_carte_giocatore(self.__giocatori[-1]) > self.get_tot_carte_giocatore(self.__giocatori[i]):
                    s_vinti += self.__scommesse[self.__giocatori[i].get_id()]
                elif self.get_tot_carte_giocatore(self.__giocatori[-1]) < self.get_tot_carte_giocatore(self.__giocatori[i]):
                    s_persi += self.__scommesse[self.__giocatori[i].get_id()]

            if s_persi > s_vinti: # SE STAI A PERDERE SOLDI PESCA CARTA
                self.set_carte(self.__giocatori[-1])
                print(self.__carte_totali[self.__giocatori[-1].get_id()])
                if self.get_tot_carte_giocatore(self.__giocatori[-1]) > 21:
                    print('Sballato')
                elif self.get_tot_carte_giocatore(self.__giocatori[-1]) == 21:
                    print('21')
            else:
                break

        print('vinto  ', s_vinti)
        print('perso  ', s_persi)
        



            

        
            

