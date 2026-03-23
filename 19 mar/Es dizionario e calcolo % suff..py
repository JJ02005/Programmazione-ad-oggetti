registro={}

n_materie=int(input("Inserisci numero delle materie:"))
if n_materie==0:
    print("Registro vuoto")
    exit(0)

for i in range(n_materie):
    materia=input("Inserisci nome della materia:")
    registro[materia]= []

    n_voti=int(input(f"Quanti voti vuoi inserire per {materia}?"))
    for j in range(n_voti):
        voto=int(input(f"Inserisci voti presi in {materia}:"))
        registro[materia].append(voto)

print("Ecco il registro stampato:", registro)


#Calcolo percentuale per ogni materia
for materia in registro:
    lista_voti=registro[materia]
    totale_voti=len(lista_voti)

    #Contiamo quanti voti sono >=18
    contatore_suff=0
    for v in lista_voti:
        if v>=18:
            contatore_suff+=1


    #Calcolo percentuale
    if totale_voti>0:
        percentuale=(contatore_suff/totale_voti)*100
        print(f"(Materia: {materia} -> {percentuale}% di voti sufficienti.")
    else:
        print(f"Materia: {materia} -> Nessun voto inserito.")