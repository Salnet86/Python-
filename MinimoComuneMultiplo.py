
'''
a = 12  # Il numero che vuoi usare
b = 18  # Un altro numero
i = max(a, b)  # Iniziamo dal numero più grande tra a e b
minimo = 0

while True:
    if i % a == 0 and i % b == 0:  # Se i è divisibile sia per a che per b
        minimo = i  # Abbiamo trovato il MCM
        break  # Esci dal ciclo
    i += 1  # Incrementa i per cercare il prossimo multiplo

print(f"Il MCM di {a} e {b} è {minimo}")

'''
d = 12
x = 1
while d > 0:
    if d % 2 == 0:
        x = d * 2  # Moltiplichiamo d per 2 se d è divisibile per 2
        print("Minimo comune multiplo (multiplo trovato):", x)
        break  # Una volta trovato il MCM, usciamo dal ciclo
    d /= 2  # Continuamo a dividere d per 2 finché è pari

