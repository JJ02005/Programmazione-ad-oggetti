"""Definire una funzione che data una stringa restituisce True se la stringa
presenta dei caratteri dupplicati, False altrimenti."""



def controlla_duplicati():
    parola = input("Inserisci una parola da analizzare: ")
    visti = []
    trovato = False

    for carattere in parola:
        if carattere in visti:
            trovato = True
            break
        visti.append(carattere)

    if trovato:
            print("Esito: La stringa ha dei duplicati,")
    else:
        print("Esito: Non ci sono duplicati.")


# Eseguiamo la funzione
controlla_duplicati()