# Creazione di una tupla
# Una tupla è una sequenza ordinata di elementi che non può essere modificata dopo la creazione
tupla1 = (1, 2, 3, 4, 5)
print("Tupla 1:", tupla1)

# Creazione di una tupla con diversi tipi di dati
tupla2 = (1, "Python", 3.14, True)
print("Tupla 2:", tupla2)

# Accesso agli elementi di una tupla
# Gli elementi di una tupla si possono accedere tramite l'indice, dove l'indice parte da 0
print("Primo elemento di tupla1:", tupla1[0])
print("Secondo elemento di tupla2:", tupla2[1])

# Slicing (estrazione di una parte della tupla)
# Possiamo prendere un sottoinsieme della tupla specificando un range di indici
tupla_sliced = tupla1[1:4]
print("Slicing di tupla1 (dal secondo al quarto elemento):", tupla_sliced)

# Verifica se un elemento è presente nella tupla
# Usiamo l'operatore 'in' per verificare se un elemento è contenuto nella tupla
print("3 è nella tupla1?", 3 in tupla1)
print("'Python' è nella tupla2?", "Python" in tupla2)

# Lunghezza della tupla
# La funzione len() restituisce il numero di elementi nella tupla
print("Lunghezza di tupla1:", len(tupla1))

# Tupla con un solo elemento
# Una tupla con un solo elemento deve avere una virgola alla fine
tupla_uno = (5,)
print("Tupla con un solo elemento:", tupla_uno)

# Concatenazione di tuple
# Possiamo concatenare due tuple utilizzando l'operatore "+"
tupla_concatenata = tupla1 + tupla2
print("Tupla concatenata:", tupla_concatenata)

# Ripetizione di una tupla
# Possiamo ripetere gli elementi di una tupla utilizzando l'operatore "*"
tupla_ripetuta = tupla1 * 2
print("Tupla ripetuta due volte:", tupla_ripetuta)

# Tupla come chiave di un dizionario
# Le tuple sono immutabili, quindi possono essere usate come chiavi nei dizionari
dizionario = {tupla1: "Valore associato alla tupla1"}
print("Dizionario con una tupla come chiave:", dizionario)

# Iterare su una tupla
# Possiamo usare un ciclo for per iterare sugli elementi di una tupla
print("Elementi di tupla1:")
for elemento in tupla1:
    print(elemento)

# Contare il numero di occorrenze di un elemento
# La funzione count() restituisce il numero di volte che un elemento appare nella tupla
print("Numero di occorrenze di 3 in tupla1:", tupla1.count(3))

# Indice di un elemento
# La funzione index() restituisce l'indice della prima occorrenza di un elemento
print("Indice del numero 4 in tupla1:", tupla1.index(4))

# Creazione di una tupla vuota
# Una tupla vuota viene creata con le parentesi tonde senza alcun elemento al suo interno
tupla_vuota = ()
print("Tupla vuota:", tupla_vuota)

# Conversione di una lista in tupla
# Possiamo convertire una lista in una tupla usando la funzione tuple()
lista = [1, 2, 3]
tupla_da_lista = tuple(lista)
print("Tupla da lista:", tupla_da_lista)

# Confronto tra tuple
# Le tuple possono essere confrontate tra loro utilizzando gli operatori di confronto
tupla3 = (1, 2, 3)
tupla4 = (1, 2, 3)
print("tupla3 è uguale a tupla4?", tupla3 == tupla4)

# Tupla annidata (tuple dentro altre tuple)
# Le tuple possono contenere altre tuple come elementi
tupla_annidata = ((1, 2), (3, 4), (5, 6))
print("Tupla annidata:", tupla_annidata)

# Modifica di una tupla
# Le tuple sono immutabili, quindi non possiamo modificarne direttamente gli elementi.
# Tuttavia, possiamo creare una nuova tupla basata sulla vecchia, ad esempio cambiando un elemento.
nuova_tupla = tupla1[:2] + (10,) + tupla1[3:]
print("Nuova tupla dopo modifica:", nuova_tupla)

# Uso di tuple in funzioni
# Le tuple sono spesso utilizzate per restituire più valori da una funzione
def funzione_tupla():
    return (1, 2, 3)

risultato = funzione_tupla()
print("Risultato della funzione:", risultato)

# Decomposizione di una tupla
# Possiamo "spacchettare" una tupla in vari elementi assegnandola a variabili
a, b, c = tupla1
print("Decomposizione della tupla1:", a, b, c)
