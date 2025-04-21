# Inizializziamo il triangolo con la prima riga
triangolo = [[1]]

# Numero di righe che vogliamo stampare
n = 5

# Costruiamo il triangolo riga per riga
for i in range(1, n):
    riga = [1]  # Ogni riga inizia con un 1
    for j in range(1, i):
        # La sottrazione tra gli elementi della riga precedente
        riga.append(triangolo[i-1][j-1] + triangolo[i-1][j])
    riga.append(1)  # Ogni riga finisce con un 1
    triangolo.append(riga)

# Stampiamo il triangolo
for riga in triangolo:
    print(riga)
