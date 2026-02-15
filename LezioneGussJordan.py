# Matrice aumentata (pivot iniziale = 0 → serve scambio)
A = [
    [0.0, 2.0, 1.0, 4.0],
    [1.0, -2.0, 3.0, 1.0],
    [2.0, 1.0, -1.0, 2.0]
]

n = len(A)

def stampa(M):
    for r in M:
        print(["{:.2f}".format(x) for x in r])
    print()

print("Matrice iniziale:")
stampa(A)

for i in range(n):

    # 🔹 Controllo pivot
    if A[i][i] == 0:
        for r in range(i + 1, n):
            if A[r][i] != 0:
                # Scambio righe
                A[i], A[r] = A[r], A[i]
                print(f"Scambio riga {i} con riga {r}")
                stampa(A)
                break
        else:
            print("Sistema impossibile o indeterminato")
            break

    # 🔹 Eliminazione sotto diagonale (tua logica)
    for j in range(i):
        fattore = A[i][j] / A[j][j]
        for k in range(n + 1):
            A[i][k] -= fattore * A[j][k]

        print(f"Elimino elemento in posizione ({i},{j})")
        stampa(A)

print("Matrice triangolare superiore finale:")
stampa(A)
