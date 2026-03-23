""""Create la classe lista_voti, che deve permettere di:
- Memorizzare diversi oggetti di tipo CEsame.
- Stampare il nome dell’esame nel quale è stato ottenuto il voto finale
più alto. Nel caso in cui il voto più alto sia lo stesso per più esami,
dovrà essere mostrato il nome di tutti gli esami nei quali è stato
conseguito quel voto."""

class CEsame:
      def __init__(self, nome_esame, voto_primo_parziale, voto_secondo_parziale):
            self.nome_esame = nome_esame
            self.voto_primo_parziale = voto_primo_parziale
            self.voto_secondo_parziale = voto_secondo_parziale

      def _calcola_media(self):
                media = (self.voto_primo_parziale + self.voto_secondo_parziale) / 2
                return media

      def stampa_voto_finale(self):
                voto_finale = self._calcola_media()
                print("Il voto finale per l'esame ", self.nome_esame, " è ", voto_finale)


class CLista_Voti:
    def __init__(self):
        self._lista = []

    def aggiungi_esame(self):
        print("\n--- Inserimento nuovo esame ---")
        nome = input("Inserisci il nome dell'esame: ")
        voto1 = float(input("Inserisci il voto del primo parziale: "))
        voto2 = float(input("Inserisci il voto del secondo parziale: "))

        # ---> COMPOSIZIONE: Creiamo l'oggetto CEsame DENTRO la lista
        nuovo_esame = CEsame(nome, voto1, voto2)
        self._lista = self._lista + [nuovo_esame]
        print("Esame aggiunto con successo!")

    def mostra_nome_esame_voto_piu_alto(self):
        if len(self._lista) == 0:
            print("\nNon ci sono esami nella lista.")
            return

        voto_massimo = 0
        esami_migliori = []

        for esame in self._lista:
            voto_attuale = esame._calcola_media()

            if voto_attuale > voto_massimo:
                # Nuovo record assoluto!
                voto_massimo = voto_attuale
                esami_migliori = [esame.nome_esame]
            elif voto_attuale == voto_massimo:
                # Pareggio! Aggiungiamo il nome alla lista dei migliori
                esami_migliori = esami_migliori + [esame.nome_esame]

        print("\n--- RISULTATO ---")
        print("Il voto più alto è", voto_massimo)
        print("Conseguito nei seguenti esami:", esami_migliori)


# --- TESTIAMO IL PROGRAMMA ---

# Creiamo il nostro registro vuoto
mio_registro = CLista_Voti()

# Aggiungiamo 3 esami
# (Suggerimento: prova a inserire due materie diverse con gli stessi voti alti
# per vedere se te le stampa entrambe alla fine!)
mio_registro.aggiungi_esame()
mio_registro.aggiungi_esame()
mio_registro.aggiungi_esame()

# Chiediamo al registro di calcolare e mostrare il vincitore
mio_registro.mostra_nome_esame_voto_piu_alto()
