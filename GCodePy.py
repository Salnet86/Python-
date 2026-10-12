import re

gcode_testo = """
G21 ; Inizializzazione mm
G90 ; Posizionamento assoluto
G1 X10.5 Y20.0 Z2.0 F1500
G0 X0 Y0
G1 X15.0 Y25.0 F1200
"""

# 1. Dividiamo il testo riga per riga
linee = gcode_testo.strip().split("\n")

for riga in linee:
    riga = riga.strip()
    
    # Ignoriamo le righe vuote
    if not riga:
        continue
        
    # Rimuoviamo eventuali commenti (tutto ciò che viene dopo il punto e virgola)
    if ";" in riga:
        riga = riga.split(";")[0].strip()

    # 2. Primo IF: controlliamo se la riga contiene o inizia con G1 (movimento lineare)
    if "G1" in riga:
        print(f"\n[Rilevato comando G1]: {riga}")
        
        # 3. IF anidato / Estrazione dei valori numerici con le regex
        # Cerchiamo le coordinate X, Y e la velocità F associate a questo G1
        x_match = re.search(r"X([-\d.]+)", riga)
        y_match = re.search(r"Y([-\d.]+)", riga)
        f_match = re.search(r"F([-\d.]+)", riga)
        
        # Salviamo i valori convertendoli in numeri decimali (float) se trovate
        x_val = float(x_match.group(1)) if x_match else None
        y_val = float(y_match.group(1)) if y_match else None
        f_val = float(f_match.group(1)) if f_match else None
        
        # Stampiamo i dati estratti per verificarli
        print(f" -> Valore X: {x_val}")
        print(f" -> Valore Y: {y_val}")
        print(f" -> Velocità F: {f_val}")
        
    elif "G0" in riga:
        # Se invece è un movimento rapido G0 gestisci qui altri controlli
        pass
