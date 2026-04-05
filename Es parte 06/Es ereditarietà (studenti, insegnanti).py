class CPersona():
    def __init__(self, nome, cognome, codice_fiscale):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale  # Aggiunto qui!

    def stampa_dati(self):
        return f"{self.nome} {self.cognome}"


class CStudente(CPersona):
    def __init__(self, nome, cognome, codice_fiscale, classe_frequentata):
        super().__init__(nome, cognome, codice_fiscale)
        self.classe_frequentata = classe_frequentata

    def stampa_dati(self):
        dati_base = super().stampa_dati()
        print(f"Lo studente {dati_base} frequenta la classe {self.classe_frequentata}")


class CInsegnante(CPersona):
    def __init__(self, nome, cognome, codice_fiscale, materia_insegnata):
        super().__init__(nome, cognome, codice_fiscale)
        self.materia_insegnata = materia_insegnata

    def stampa_dati(self):
        dati_base = super().stampa_dati()
        print(f"L'insegnante {dati_base} insegna {self.materia_insegnata}")


class CAnagrafica():
    def __init__(self):
        self._persone = {}

    def _chiedi_dati_comuni(self):
        n = input("Nome: ")
        c = input("Cognome: ")
        cf = input("Codice Fiscale: ")
        return n, c, cf

    def _crea_insegnante(self):
        n, c, cf = self._chiedi_dati_comuni()
        materia = input("Materia: ")
        return CInsegnante(n, c, cf, materia)

    def _crea_studente(self):
        n, c, cf = self._chiedi_dati_comuni()
        classe = input("Classe: ")
        return CStudente(n, c, cf, classe)

    def aggiungi_persona(self):
        tipo = input("Insegnante o Studente? ").lower()
        if tipo == 'insegnante':
            persona = self._crea_insegnante()
        elif tipo == 'studente':
            persona = self._crea_studente()
        else:
            print("Tipo errato")
            return  # Esci se sbagli tipo


        self._persone[persona.codice_fiscale] = persona

    def cerca_persona(self):
        cf = input("Inserisci il CF da cercare: ")
        if cf in self._persone:
            self._persone[cf].stampa_dati()
        else:
            print("Codice fiscale non trovato.")


# --- Esecuzione ---
anagrafica = CAnagrafica()
anagrafica.aggiungi_persona()
anagrafica.cerca_persona()