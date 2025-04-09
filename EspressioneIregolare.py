import re

testo ="numero da trovare e 5"
risultato=re.search(r'[0-9]', testo)
if risultato:
    print("Nemuero trovato")
else:
    print("Numero non trovato")
    


txt = "abc"
#Test = re.search(r'[a-z]', testo)
Test= re.findall(r'[a-z]',txt)
if Test:
    print(Test)
    #print(Test.group())
else:
    print("Nessun carattere trovato")

