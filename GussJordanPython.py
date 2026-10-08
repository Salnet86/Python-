def eliminazione_gauss(m):
  n = len(m)

  for i in range(n):
    # 1. Individuiamo il pivot sulla diagonale principale
    pivot = m[i][i]

    if pivot == 0:
      print(f"Attenzione: pivot zero alla riga {i}!")
      continue

    # 2. Scendiamo sulle righe sottostanti per azzerare gli elementi
    for riga_corrente in range(i + 1, n):
      # Calcoliamo il fattore (divisione)
      fattore = m[riga_corrente][i] / pivot

      # Aggiorniamo tutta la riga scorrendo le colonne
      for col in range(i, len(m[0])):
        # Sottrazione della riga del pivot moltiplicata per il fattore
        m[riga_corrente][col] = m[riga_corrente][col] - (fattore * m[i][col])

  return m


# Esempio di utilizzo:
sistema = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3],
]

print("Matrice iniziale per Gauss:")
for r in sistema:
  print(r)

eliminazione_gauss(sistema)

print("\nMatrice ridotta a scala (con Gauss):")
for r in sistema:
  # Arrotondiamo per pulizia visiva dei numeri decimali
  print([round(x, 2) for x in r])
