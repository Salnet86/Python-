import re

# Un esempio di stringa contenente codice G-code con commenti
testo_gcode = """
G21 ; Unità in millimetri
G90 ; Posizionamento assoluto
T1 M6 ; Cambio utensile numero 1
G01 X10.5 Y20.0 F1500
G7 X5.2 Z-2.0
"""

# Pattern regex per trovare una lettera maiuscola (es. G, T, M) 
# seguita da uno o più numeri (es. 21, 1, 01)
pattern = r"\b[A-Z]\d+\b"

# Estraiamo tutte le corrispondenze trovate nel testo
codici_trovati = re.findall(pattern, testo_gcode)

print("Codici estratti:", codici_trovati)
# Output: ['G21', 'G90', 'T1', 'M6', 'G01', 'G7']
