class CStatisticheAcquisti():

    def __init__(self, lista_prezzi):
        self._lista_prezzi = lista_prezzi

    def calcola_prezzo_medio(self):
        prezzo_totale = 0
        for prezzo in self._lista_prezzi:
            prezzo_totale = prezzo_totale + prezzo
        return prezzo_totale / len(self._lista_prezzi)

    def stampa_prezzo_medio(self):
        prezzo_medio = self.calcola_prezzo_medio()
        print("Il prezzo medio è ", prezzo_medio)



oggetto_stat_acquisti = CStatisticheAcquisti([4, 8])
oggetto_stat_acquisti.stampa_prezzo_medio()