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


class CCliente:
    def __init__(self,nome, cognome, numero_telefono):
        self.nome = nome
        self.cognome = cognome
        self.numero_telefono = numero_telefono

class CListaCliente:
    def __init__(self):
        self._lista = []

    def aggiungi_cliente(self):
        print("\n--- Inserimento nuovo cliente ---")
        nome = input("Inserisci il nome del cliente: ")
        cognome = input("Inserisci il cognome del cliente: ")
        numero_telefono = input("Inserisci il numero di telefono del cliente: ")

        nuovo_cliente = CCliente(nome, cognome, numero_telefono)
        self._lista = self._lista + [nuovo_cliente]
        print("Cliente aggiunto con successo!")

class CVendita:
    def __init__(self, cliente, libro):
        self.cliente = cliente
        self.libro = libro

    def stampa_riepilogo(self):
        print("\n--- Vendita effettuata---")
        print("Cliente: ", self.cliente.nome, " ", self.cliente.cognome)
        print("Libro: ", self.libro.titolo)


# --- TESTIAMO IL CODICE ---

registro_libri=CListaLibri()
registro_libri.aggiungi_libro()

registro_clienti=CListaCliente()
registro_clienti.aggiungi_cliente()

titolo_venduto=input("Quale libro è stato venduto?(Inserisci il titolo):")

#La stringa seguente mi serve per pescare l'oggetto libro venduto
libro_venduto=registro_libri._cerca_libro(titolo_venduto)

if len(registro_clienti._lista) > 0 and libro_venduto is not None:
    cliente_scelto = registro_clienti._lista[0]

    nuova_vendita = CVendita(cliente_scelto, libro_venduto)

# 4. Verifichiamo accedendo ai dati "a catena"
    print(f"Vendita registrata!")
    print(f"Cliente: {nuova_vendita.cliente.nome}")
    print(f"Libro: {nuova_vendita.libro.titolo}")
else:
    print("Errore: Libro non trovato o nessun cliente registrato.")
