i = 0
while i < 5:
    if i == 3:
        i += 1  # Incrementa prima di saltare
        continue  # Salta il numero 3
    print(i)
    i += 1
