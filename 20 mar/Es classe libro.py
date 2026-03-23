#  LA CLASSE BASE: CLibr
class CLibro:
    def __init__(self, titolo, autore, editore, prezzo, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.prezzo = prezzo
        self.anno_pubblicazione = anno_pubblicazione

    def _calcola_eta_libro(self, anno_corrente):
        eta_libro = anno_corrente - self.anno_pubblicazione
        return eta_libro

    def _calcola_sconto(self, anno_corrente):
        eta_libro = self._calcola_eta_libro(anno_corrente)
        if eta_libro > 5:
            sconto = self.prezzo * 5 / 100
        else:
            sconto = 0
        return sconto

    def calcola_prezzo_scontato(self, anno_corrente):
        prezzo_scontato = self.prezzo - self._calcola_sconto(anno_corrente)
        return prezzo_scontato


# LA CLASSE CONTENITORE: CListaLibri (Composizione)
class CListaLibri:
    def __init__(self):
        self._lista = []

    def aggiungi_libro(self):
        oggetto_libro = self._crea_nuovo_oggetto_libro()
        self._lista = self._lista + [oggetto_libro]

    def _crea_nuovo_oggetto_libro(self):
        titolo = input("inserisci il titolo del libro: ")
        autore = input("inserisci l'autore del libro: ")
        editore = input("inserisci l'editore del libro: ")
        prezzo = float(input("inserisci il prezzo del libro: "))
        anno_pubblicazione = int(input("inserisci l'anno di pubblicazione del libro: "))

        # Ora Python sa cos'è CLibro perché l'abbiamo definito sopra!
        oggetto_libro = CLibro(titolo, autore, editore, prezzo, anno_pubblicazione)
        return oggetto_libro

    def _cerca_libro(self, titolo):
        for libro in self._lista:
            if libro.titolo == titolo:
                return libro
        print("Libro non trovato!")

    def mostra_prezzo_libro(self, titolo, anno_corrente):
        oggetto_libro = self._cerca_libro(titolo)
        if oggetto_libro is not None:
            print(oggetto_libro.calcola_prezzo_scontato(anno_corrente))


# --- TESTIAMO IL CODICE ---

# Creiamo lo scaffale vuoto (la lista)
mia_lista = CListaLibri()

# Aggiungiamo un libro (il terminale ti chiederà di inserire i dati)
print("--- AGGIUNGI UN LIBRO ---")
mia_lista.aggiungi_libro()

# Mostriamo il prezzo scontato del libro che hai appena inserito
titolo_da_cercare = input("\nInserisci il titolo del libro per vederne il prezzo scontato: ")
print("Il prezzo finale è:")
mia_lista.mostra_prezzo_libro(titolo_da_cercare, 2026)