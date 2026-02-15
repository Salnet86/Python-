# Definiamo una matrice 4x4 di esempio (A)
# In un contesto reale (es. elettronica), questi potrebbero essere i coefficienti 
# delle leggi di Kirchhoff per un circuito.
A = [
    [2.0,  1.0, -1.0,  8.0],
    [-3.0, -1.0,  2.0, -11.0],
    [-2.0,  1.0,  2.0, -3.0],
    [1.0,  1.0, -1.0,  6.0]
]

n = len(A)

print("Matrice Originale:")
for riga in A: print(riga)
print("-" * 30)

for i in range(n):
    # 1. Ricerca del Pivot (Massimo sulla colonna)
    riga_pivot = i
    for k in range(i + 1, n):
        if abs(A[k][i]) > abs(A[riga_pivot][i]):
            riga_pivot = k
    
    # Scambio delle righe (Swapping)
    A[i], A[riga_pivot] = A[riga_pivot], A[i]
    
    # 2. Annullamento elementi sotto il pivot (Triangolarizzazione)
    for j in range(i + 1, n):
        # Evitiamo divisioni per zero se la matrice è singolare
        if A[i][i] == 0:
            continue
            
        moltiplicatore = A[j][i] / A[i][i]
        
        # Sottraiamo la riga i-esima moltiplicata per il fattore dalla riga j-esima
        for k in range(i, n):
            A[j][k] = A[j][k] - moltiplicatore * A[i][k]

print("Matrice Triangolarizzata (Gauss):")
for riga in A:
    # Formattazione a 2 decimali per leggibilità
    print([round(val, 2) for val in riga])
