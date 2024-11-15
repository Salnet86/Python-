# Definiamo l'elemento da cercare e l'array ordinato
x =15  # Il numero che vogliamo cercare
a = [1, 5, 8, 10, 15]  # Array ordinato
N = len(a)  # Lunghezza dell'array

# Inizializzazione degli indici
i = 0
j = N - 1
pos = -1  # Inizializziamo la posizione a -1 (significa che l'elemento non è trovato)

# Ricerca binaria
while i <= j:
    m = (i + j) // 2  # Calcoliamo l'indice medio

    if a[m] == x:  # Se l'elemento è trovato
        pos = m  # Memorizziamo la posizione
        break  # Uscire dal ciclo
    elif a[m] < x:  # Se l'elemento da cercare è maggiore
        i = m + 1  # Modifichiamo l'intervallo di ricerca
    else:  # Se l'elemento da cercare è minore
        j = m - 1  # Modifichiamo l'intervallo di ricerca

# Stampa il risultato
if pos != -1:
    print(f"Numero trovato in posizione: {pos}")
else:
    print("Numero non trovato")
