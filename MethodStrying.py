# Esempi di metodi di stringhe in Python

# 1. Creazione di stringhe
stringa1 = "Ciao"
stringa2 = 'Mondo'
stringa3 = """Questo è un esempio di stringa
su più righe."""
print("Stringa multilinea:", stringa3)

# 2. Metodo .lower() - Converte tutta la stringa in minuscolo
stringa = "CIAO"
print("\nStringa in minuscolo:", stringa.lower())

# 3. Metodo .upper() - Converte tutta la stringa in maiuscolo
stringa = "ciao"
print("\nStringa in maiuscolo:", stringa.upper())

# 4. Metodo .capitalize() - Capitalizza solo la prima lettera della stringa
stringa = "ciao mondo"
print("\nStringa con prima lettera maiuscola:", stringa.capitalize())

# 5. Metodo .title() - Capitalizza la prima lettera di ogni parola
stringa = "ciao mondo, come va?"
print("\nStringa con titolo capitalizzato:", stringa.title())

# 6. Metodo .strip() - Rimuove gli spazi all'inizio e alla fine della stringa
stringa = "  ciao mondo  "
print("\nStringa senza spazi iniziali e finali:", stringa.strip())

# 7. Metodo .replace() - Sostituisce una parte della stringa con un'altra
stringa = "Ciao Mondo"
print("\nStringa con sostituzione:", stringa.replace("Mondo", "Python"))

# 8. Metodo .split() - Divide una stringa in una lista, separandola dove trova lo spazio (o un altro separatore)
stringa = "Ciao Mondo Python"
print("\nLista divisa dalla stringa:", stringa.split())

# 9. Metodo .join() - Unisce una lista di stringhe in una singola stringa, separandole con un delimitatore
lista = ["Ciao", "Mondo", "Python"]
print("\nLista unita in una stringa:", " ".join(lista))

# 10. Metodo .find() - Restituisce l'indice della prima occorrenza di un sottostringa, oppure -1 se non trovata
stringa = "Ciao Mondo"
print("\nIndice della sottostringa 'Mondo':", stringa.find("Mondo"))

# 11. Metodo .count() - Conta quante volte un sottostringa appare nella stringa
stringa = "Ciao Mondo, Ciao Python"
print("\nNumero di volte che appare 'Ciao':", stringa.count("Ciao"))

# 12. Metodo .startswith() - Controlla se la stringa inizia con un certo prefisso
stringa = "Ciao Mondo"
print("\nLa stringa inizia con 'Ciao'?", stringa.startswith("Ciao"))

# 13. Metodo .endswith() - Controlla se la stringa finisce con un certo suffisso
stringa = "Ciao Mondo"
print("\nLa stringa finisce con 'Mondo'?", stringa.endswith("Mondo"))

# 14. Metodo .isalpha() - Restituisce True se la stringa contiene solo lettere
stringa = "Ciao"
print("\nLa stringa contiene solo lettere?", stringa.isalpha())

# 15. Metodo .isdigit() - Restituisce True se la stringa contiene solo numeri
stringa = "12345"
print("\nLa stringa contiene solo numeri?", stringa.isdigit())

# 16. Metodo .isspace() - Restituisce True se la stringa contiene solo spazi
stringa = "    "
print("\nLa stringa contiene solo spazi?", stringa.isspace())

# 17. Metodo .isupper() - Restituisce True se tutti i caratteri della stringa sono maiuscoli
stringa = "CIAO"
print("\nLa stringa è tutta maiuscola?", stringa.isupper())

# 18. Metodo .islower() - Restituisce True se tutti i caratteri della stringa sono minuscoli
stringa = "ciao"
print("\nLa stringa è tutta minuscola?", stringa.islower())

# 19. Metodo .zfill() - Aggiunge zeri all'inizio della stringa fino a raggiungere una lunghezza specificata
stringa = "42"
print("\nStringa con zeri aggiunti:", stringa.zfill(5))

# 20. Metodo .rjust() - Allinea la stringa a destra, aggiungendo spazi a sinistra
stringa = "Ciao"
print("\nStringa allineata a destra:", stringa.rjust(10))

# 21. Metodo .ljust() - Allinea la stringa a sinistra, aggiungendo spazi a destra
stringa = "Ciao"
print("\nStringa allineata a sinistra:", stringa.ljust(10))

# 22. Metodo .center() - Allinea la stringa al centro, aggiungendo spazi su entrambi i lati
stringa = "Ciao"
print("\nStringa centrata:", stringa.center(10))

# 23. Metodo .partition() - Divide la stringa in una tupla con 3 elementi: la parte prima, il separatore, e la parte dopo
stringa = "Ciao Mondo Python"
print("\nStringa divisa con partition:", stringa.partition("Mondo"))

# 24. Metodo .expandtabs() - Espande i caratteri di tabulazione con uno spazio
stringa = "Ciao\tMondo"
print("\nStringa con tabulazioni espanse:", stringa.expandtabs(4))

# 25. Metodo .format() - Permette di inserire variabili all'interno di una stringa usando i segnaposti
nome = "Maria"
saluto = "Ciao, {}!".format(nome)
print("\nStringa formattata:", saluto)

# 26. Metodo f-string (dal Python 3.6) - Un'altra modalità di formattazione delle stringhe
nome = "Maria"
saluto = f"Ciao, {nome}!"
print("\nStringa formattata con f-string:", saluto)

# 27. Metodo .removeprefix() (dal Python 3.9) - Rimuove un prefisso dalla stringa
stringa = "TestCiao"
print("\nRimuovi il prefisso 'Test':", stringa.removeprefix("Test"))

# 28. Metodo .removesuffix() (dal Python 3.9) - Rimuove un suffisso dalla stringa
stringa = "CiaoTest"
print("\nRimuovi il suffisso 'Test':", stringa.removesuffix("Test"))
