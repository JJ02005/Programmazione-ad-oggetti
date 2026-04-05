class CCliente:
    def __init__(self, idx, numero_telefono):
        self.idx = idx
        self.numero_telefono = numero_telefono

        # Definisco un nuovo attributo per sfruttare l'ereditarietà
        self.tipo_cliente= "tipo_cliente"

    def stampa_telefono(self):
        print(f"Il numero di telefono di {self.tipo_cliente} {self.idx}  è: {self.numero_telefono}")

class CAzienda(CCliente):
    def __init__(self,partita_iva, idx, numero_telefono):
        super().__init__(idx, numero_telefono)
        self.partita_iva = partita_iva
        self.tipo_cliente = "azienda"



class CPersona(CCliente):
    def __init__(self, nome, cognome, anno_nascita, idx, numero_telefono):
        super().__init__(idx, numero_telefono)
        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita
        self.tipo_cliente = "persona"



oggetto_azienda = CAzienda("12345678901", "123", "070998899")
oggetto_persona = CPersona("Mario", "Rossi", 1980, "456", "333123456")

oggetto_azienda.stampa_telefono()
oggetto_persona.stampa_telefono()