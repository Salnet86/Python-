n = 5

for i in range(n):
    riga = [1]  # Ogni riga inizia sempre da 1
    valore = 1  # Il primo coefficiente è sempre 1
    for j in range(1, i + 1):
        valore = valore * (i - j + 1) // j
        riga.append(valore)
    print(riga)
