temperatura = 12  # temperatura iniziale
limite = 0.08     # valore limite
while temperatura > limite:
    print("Temperatura:", temperatura)
    temperatura /= 2  # riduce la temperatura a metà ogni volta
print("Temperatura raggiunta:", temperatura)
