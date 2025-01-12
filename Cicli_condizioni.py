# Esempi di cicli in Python con incremento e decremento

# 1. Ciclo for con incremento
# In questo esempio usiamo un ciclo for per iterare da 0 a 4, incrementando di 1 ad ogni passo.
print("Ciclo for con incremento:")
for i in range(5):  # range(5) genera numeri da 0 a 4
    print(i)  # Stampa i valori di i da 0 a 4

# 2. Ciclo for con incremento personalizzato
# Usiamo il parametro step del range per incrementare di 2 ad ogni passo
print("\nCiclo for con incremento di 2:")
for i in range(0, 10, 2):  # Inizia da 0, termina prima di 10, incrementando di 2
    print(i)  # Stampa 0, 2, 4, 6, 8

# 3. Ciclo for su una lista
# Iteriamo su una lista e stampiamo ogni elemento
lista = [10, 20, 30, 40, 50]
print("\nCiclo for su una lista:")
for numero in lista:
    print(numero)  # Stampa ogni numero nella lista

# 4. Ciclo for con decremento
# Qui iteriamo in ordine inverso, partendo da 10 e arrivando a 1, decrementando di 1 ad ogni passo
print("\nCiclo for con decremento:")
for i in range(10, 0, -1):  # Inizia da 10, termina prima di 0, decrementando di 1
    print(i)  # Stampa i valori da 10 a 1

# 5. Ciclo while con incremento
# In questo esempio usiamo un ciclo while per incrementare una variabile finché non raggiunge 5
print("\nCiclo while con incremento:")
i = 0
while i < 5:  # Continua finché i è minore di 5
    print(i)  # Stampa i
    i += 1  # Incrementa i di 1

# 6. Ciclo while con decremento
# Qui decrementiamo una variabile finché non arriva a 0
print("\nCiclo while con decremento:")
i = 5
while i > 0:  # Continua finché i è maggiore di 0
    print(i)  # Stampa i
    i -= 1  # Decrementa i di 1

# 7. Ciclo for con condizione di salto (continue)
# Utilizziamo "continue" per saltare l'iterazione corrente quando i è uguale a 3
print("\nCiclo for con continue:")
for i in range(5):
    if i == 3:
        continue  # Salta il numero 3
    print(i)  # Stampa i tranne il 3

# 8. Ciclo for con condizione di interruzione (break)
# In questo esempio usiamo "break" per interrompere il ciclo quando i raggiunge 3
print("\nCiclo for con break:")
for i in range(5):
    if i == 3:
        break  # Interrompe il ciclo quando i è uguale a 3
    print(i)  # Stampa i fino a 2

# 9. Ciclo while con condizione di interruzione (break)
# Anche in un ciclo while possiamo usare break per interrompere il ciclo
print("\nCiclo while con break:")
i = 0
while True:  # Ciclo infinito
    if i == 3:
        break  # Interrompe il ciclo quando i è uguale a 3
    print(i)  # Stampa i
    i += 1  # Incrementa i

# 10. Ciclo for con più variabili (tuple unpacking)
# Qui iteriamo su una lista di tuple e "spacchettiamo" ogni tupla in due variabili
print("\nCiclo for con tuple unpacking:")
lista_tuple = [(1, 'a'), (2, 'b'), (3, 'c')]
for numero, lettera in lista_tuple:
    print(f"Numero: {numero}, Lettera: {lettera}")

# 11. Ciclo for con calcolo di somma
# Utilizziamo un ciclo for per calcolare la somma dei numeri in una lista
print("\nCiclo for con somma dei numeri:")
somma = 0
for numero in [1, 2, 3, 4, 5]:
    somma += numero  # Aggiunge ogni numero alla somma
print("Somma totale:", somma)

# 12. Ciclo for con indice e valore (enumerate)
# Usando enumerate() possiamo ottenere sia l'indice che il valore durante l'iterazione
print("\nCiclo for con indice e valore (enumerate):")
for indice, valore in enumerate([10, 20, 30, 40]):
    print(f"Indice: {indice}, Valore: {valore}")

# 13. Ciclo while con un contatore
# In questo esempio, usiamo un ciclo while per contare fino a 10 e fermarci quando il contatore raggiunge 10
print("\nCiclo while con contatore:")
contatore = 0
while contatore < 10:
    print(contatore)  # Stampa il contatore
    contatore += 1  # Incrementa il contatore

# 14. Ciclo while con condizione complessa
# Un ciclo while con una condizione composta da due verifiche
print("\nCiclo while con condizione complessa:")
i = 0
while i < 5 and i != 3:  # Continua finché i è minore di 5 e diverso da 3
    print(i)
    i += 1

# 15. Ciclo for con calcolo di prodotto
# In questo esempio, calcoliamo il prodotto dei numeri in una lista
print("\nCiclo for con prodotto dei numeri:")
prodotto = 1
for numero in [1, 2, 3, 4, 5]:
    prodotto *= numero  # Moltiplica ogni numero al prodotto
print("Prodotto totale:", prodotto)
