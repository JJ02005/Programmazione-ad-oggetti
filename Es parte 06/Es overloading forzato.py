from functools import singledispatchmethod



class CFormattatore():
    @singledispatchmethod
    def stampa_dati(self, dato):
        print("Dato non supportato")

    @stampa_dati.register
    def _stampa_dati(self, dato:list):
        print("Gli elementi della lista sono:")
        for i in dato:
            print(i)

    @stampa_dati.register
    def _stampa_dati(self, dato: dict):
        print("Gli elementi del dizionario sono:")
        for chiave in dato:
            print(f"{chiave}: {dato[chiave]}")

# --- TESTIAMO IL CODICE ---

formattatore = CFormattatore()
formattatore.stampa_dati([1,2,3])
formattatore.stampa_dati({"a":1,"b":2,"c":3})
