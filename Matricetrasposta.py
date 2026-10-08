def trasponi_matrice(m):
  n = len(m)

  for i in range(n):
    # Partiamo da i + 1 per evitare doppi scambi e la diagonale
    for j in range(i + 1, n):
      # Salviamo al sicuro l'elemento con la temp
      temp = m[i][j]
      # Spostiamo l'elemento specchiato dalla parte opposta
      m[i][j] = m[j][i]
      # Rimettiamo il valore salvato nella posizione opposta
      m[j][i] = temp

  return m


# Esempio di utilizzo:
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matrice originale:")
for r in matrice:
  print(r)

trasponi_matrice(matrice)

print("\nMatrice trasposta (colonne diventate righe):")
for r in matrice:
  print(r)
