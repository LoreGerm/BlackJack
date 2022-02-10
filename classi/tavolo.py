# dizionario con chiave id giocatore e valore lista carte

class Tavolo:


    def __init__(self, banco, giocatori):
        self.__scommesse = {}
        self.__giocatori = giocatori
        self.__banco = banco
        self.__carte_totali = {}

    def get_carte(self):
        return self.__carte_totali


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


