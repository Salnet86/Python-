import re

testo ="numero da trovare e 5"
risultato=re.search(r'[0-9]', testo)
if risultato:
    print("Nemuero trovato")
else:
    print("Numero non trovato")
    

