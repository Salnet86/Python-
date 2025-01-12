import time

# Funzione per il cronometro
def cronometro():
    ore = 0
    minuti = 0
    secondi = 0
    
    while True:
        # Aspetta 1 secondo
        time.sleep(1)
        
        # Incrementa i secondi
        secondi += 1
        
        # Gestisce il passaggio dei secondi ai minuti
        if secondi == 60:
            secondi = 0
            minuti += 1
        
        # Gestisce il passaggio dei minuti alle ore
        if minuti == 60:
            minuti = 0
            ore += 1
        
        # Stampa il tempo trascorso in formato ore:minuti:secondi su un'unica riga
        print(f"\r{ore:02}:{minuti:02}:{secondi:02}", end="", flush=True)

# Avvia il cronometro
cronometro()
