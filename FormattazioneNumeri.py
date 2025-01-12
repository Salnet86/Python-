# Esempi di formattazione dei numeri in Python

# 1. Formattazione con il metodo format() per numeri con decimali
numero = 1234.56789
# Formattare il numero con 2 decimali
print("\nFormattazione con 2 decimali usando format:", "{:.2f}".format(numero))

# 2. Formattazione con f-string per numeri con decimali
print(f"Formattazione con 2 decimali (f-string): {numero:.2f}")

# 3. Formattazione con separatori delle migliaia (usando format())
numero_grande = 1234567.89
print("\nNumero con separatore delle migliaia usando format:", "{:,}".format(numero_grande))

# 4. Formattazione come percentuale
percentuale = 0.1234
# Formattazione con 2 decimali come percentuale
print(f"\nPercentuale con 2 decimali: {percentuale:.2%}")

# 5. Formattazione con una larghezza fissa e zeri
numero = 42
# Formattare il numero con larghezza 5, riempiendo con zeri
print(f"\nNumero con larghezza fissa (riempito con zeri): {numero:05d}")

# 6. Formattazione con larghezza fissa e allineamento a destra
numero = 42
# Formattare il numero con larghezza 5, allineato a destra
print(f"\nNumero allineato a destra con larghezza 5: {numero:5d}")

# 7. Formattazione con larghezza fissa e allineamento a sinistra
numero = 42
# Formattare il numero con larghezza 5, allineato a sinistra
print(f"\nNumero allineato a sinistra con larghezza 5: {numero:<5d}")

# 8. Formattazione con larghezza fissa e centratura
numero = 42
# Formattare il numero con larghezza 5, centrato
print(f"\nNumero centrato con larghezza 5: {numero:^5d}")

# 9. Formattazione con notazione scientifica
numero = 12345.6789
# Formattazione con notazione scientifica (3 decimali)
print(f"\nNotazione scientifica con 3 decimali: {numero:.3e}")

# 10. Formattazione con un numero fisso di decimali
numero = 12.34567
# Arrotondare e formattare con 2 decimali
print(f"\nNumero arrotondato a 2 decimali: {numero:.2f}")

# 11. Formattazione con il segno più per numeri positivi e negativi
numero_pos = 45
numero_neg = -45
# Mostrare il segno + per numeri positivi e negativi
print(f"\nNumero positivo con segno: {numero_pos:+d}")
print(f"Numero negativo con segno: {numero_neg:+d}")

# 12. Formattazione con spazio per numeri positivi
print(f"\nNumero positivo con spazio (senza segno): {numero_pos: d}")
print(f"Numero negativo con spazio: {numero_neg: d}")

# 13. Formattazione con precisione per i numeri float
numero = 3.14159265358979
# Limitiamo la precisione a 4 decimali
print(f"\nNumero con precisione di 4 decimali: {numero:.4f}")

# 14. Formattazione con tipo di dato fisso per i numeri interi
numero_intero = 42
# Formattiamo come intero fisso
print(f"\nNumero intero con formato fisso: {numero_intero:d}")

# 15. Formattazione di un numero come valuta
numero_valuta = 1234567.89
# Formattiamo il numero come valuta con separatori di migliaia
print(f"\nNumero come valuta (separatore di migliaia): {numero_valuta:,.2f}")
