n = int(input('Inserisci un valore per il Triangolo di tartaglia   :'))
tartaglia = []

for i in range(n):  # Partiamo da 0
    triangolo = []  # Ogni volta iniziamo una nuova riga

    for j in range(i + 1):  # Da 0 a i
        if j == 0 or j == i:  # Primo o ultimo elemento della riga
            triangolo.append(1)
        else:
            valore = tartaglia[i-1][j-1] + tartaglia[i-1][j]  # Somma dei due numeri sopra
            triangolo.append(valore)

    tartaglia.append(triangolo)  # Aggiungi la riga completa a tartaglia

# Stampa il triangolo di Tartaglia
for ta in tartaglia:
    print(ta)
