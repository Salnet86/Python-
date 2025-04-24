# Dati di esempio
y_values = [23, 21, 19, 18, 20]
max_y = max(y_values)

# Creazione del grafico ASCII
for i in range(max_y, 0, -1):
    line = ""
    for y in y_values:
        if y >= i:
            line += "* "
        else:
            line += "  "
    print(f"{i:2d} | {line}")
