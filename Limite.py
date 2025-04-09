finito = 12
limite = 0

while finito > 0:
    limite = finito
    if limite == 0.09375:
        print('Limite trovato e calcolato:', limite)
        finito = 0  # Impostiamo finito a 0 per uscire dal ciclo
    finito /= 2  # Dividiamo finito per 2 ad ogni iterazione
