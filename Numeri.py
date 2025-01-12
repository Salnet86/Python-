# Esempi di operazioni sui numeri e formattazione dei numeri in Python

# 1. Lavorare con numeri interi
numero_intero = 10
print("Numero intero:", numero_intero)

# Aggiungere un numero intero
numero_intero += 5
print("\nAggiungiamo 5:", numero_intero)

# Sottrarre un numero intero
numero_intero -= 3
print("Sottrai 3:", numero_intero)

# Moltiplicare un numero intero
numero_intero *= 2
print("Moltiplica per 2:", numero_intero)

# Dividere un numero intero
numero_intero /= 4
print("Dividi per 4:", numero_intero)

# Dividere e ottenere il quoziente (solo la parte intera)
numero_intero = 10
quoziente = numero_intero // 3
print("\nQuoziente di 10 diviso 3 (parte intera):", quoziente)

# Resto della divisione (modulo)
resto = numero_intero % 3
print("Resto della divisione di 10 per 3:", resto)

# Elevamento a potenza
potenza = numero_intero ** 2
print("\nElevamento a potenza di 10^2:", potenza)

# 2. Lavorare con numeri in virgola mobile (float)
numero_float = 10.5
print("\nNumero in virgola mobile:", numero_float)

# Aggiungere un numero in virgola mobile
numero_float += 2.5
print("Aggiungi 2.5:", numero_float)

# Moltiplicare un numero in virgola mobile
numero_float *= 1.5
print("Moltiplica per 1.5:", numero_float)

# Dividere un numero in virgola mobile
numero_float /= 3
print("Dividi per 3:", numero_float)

# 3. Conversione tra tipi numerici
numero_intero = 10
numero_float = float(numero_intero)  # Convertiamo un intero in float
print("\nConversione da intero a float:", numero_float)

numero_float = 10.5
numero_intero = int(numero_float)  # Convertiamo un float in intero (approssimato)
print("Conversione da float a intero:", numero_intero)

# 4. Funzioni matematiche comuni
import math

# Radice quadrata
radice = math.sqrt(25)
print("\nRadice quadrata di 25:", radice)

# Valore assoluto
valore_assoluto = abs(-10)
print("Valore assoluto di -10:", valore_assoluto)

# Funzione per il massimo tra due numeri
massimo = max(10, 20)
print("\nMassimo tra 10 e 20:", massimo)

# Funzione per il minimo tra due numeri
minimo = min(10, 20)
print("Minimo tra 10 e 20:", minimo)

# Arrotondare un numero
arrotondato = round(3.14159, 2)  # Arrotonda a 2 decimali
print("\nArrotondamento di 3.14159 a 2 decimali:", arrotondato)

# 5. Formattazione di numeri

# Formattazione con il metodo format() (2 decimali)
numero = 1234.56789
print("\nFormattazione con 2 decimali:", "{:.2f}".format(numero))

# Formattazione con f-string (2 decimali)
print(f"Formattazione con 2 decimali (f-string): {numero:.2f}")

# Separatore delle migliaia
numero_grande = 1234567.89
print("\nNumero con separatore delle migliaia:", "{:,}".format(numero_grande))

# Formattazione come percentuale
percentuale = 0.1234
print(f"\nPercentuale (con 2 decimali): {percentuale:.2%}")

# Formattazione con una larghezza fissa (riempito con zeri)
numero = 42
print("\nNumero con larghezza fissa e zeri:", f"{numero:05d}")  # 5 caratteri, riempito con zeri

# Formattazione con una larghezza fissa e allineamento a destra
numero = 42
print("\nNumero allineato a destra con larghezza 5:", f"{numero:5d}")

# 6. Controllare se un numero è intero o decimale
numero = 42
print("\nIl numero è intero?", isinstance(numero, int))

numero = 42.0
print("Il numero è decimale?", isinstance(numero, float))

# 7. Operazioni con numeri complessi
numero_complesso = 3 + 4j
print("\nNumero complesso:", numero_complesso)

# Parte reale
print("Parte reale del numero complesso:", numero_complesso.real)

# Parte immaginaria
print("Parte immaginaria del numero complesso:", numero_complesso.imag)

# 8. Gestire numeri con precisione elevata (Decimal)
from decimal import Decimal

# Usare Decimal per maggiore precisione
numero_decimale = Decimal('0.123456789012345678901234567890')
print("\nNumero con precisione elevata (Decimal):", numero_decimale)

# Sommare numeri con Decimal
numero_decimale2 = Decimal('0.987654321098765432109876543210')
somma_decimal = numero_decimale + numero_decimale2
print("Somma di due numeri con Decimal:", somma_decimal)
