n = 4

matrice = [
    [2, 1, 1, 3],
    [4, 8, 3, 2],
    [2, 3, 7, 1],
    [6, 5, 2, 9]
]

print("--- MATRICE DI PARTENZA ---")
for riga in matrice:
    print(riga)

print("\n--- INIZIO ELABORAZIONE ---")

for i in range(n):
    pivot = matrice[i][i]

    print(f"\n--> Pivot della riga {i}: {pivot}")

    # Scorro le righe sotto quella del pivot
    for j in range(i + 1, n):

        # Calcolo quanto devo moltiplicare la riga del pivot
        fattore = matrice[j][i] / pivot

        print(f"   Rendo zero matrice[{j}][{i}]")
        print(f"   Fattore = {fattore}")

        # Modifico tutta la riga j
        for k in range(i, n):
            matrice[j][k] = matrice[j][k] - fattore * matrice[i][k]

        print(f"   Riga {j} dopo la modifica: {matrice[j]}")

print("\n--- MATRICE TRIANGOLARE SUPERIORE ---")
for riga in matrice:
    print(riga)
