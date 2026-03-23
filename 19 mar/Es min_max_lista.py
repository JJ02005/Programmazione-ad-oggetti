""""Implementate la funzione min_max_lista che riceve in input una lista che
contiene almeno un elemento e restituisce in output il minimo e il massimo
valore presenti nella lista."""


def min_max_lista():
    lista = []
    n_elementi= int(input("Quanti elementi vuoi inserire nella lista?"))

    for i in range(n_elementi):
        elemento=int(input("Inserisci un elemento"))
        lista.append(elemento)

    minimo = min(lista)
    massimo = max(lista)
    return minimo, massimo


risultato = min_max_lista()
print(f"Il minimo e il massimo sono: {risultato}")





