# Ciclo for per stampare una piramide di asterischi
n = 5  # Numero di righe

for i in range(1, n + 1):
    # Stampa gli asterischi per la riga corrente
    print('*' * i)


*
**
***
****
*****




# Ciclo for per stampare una piramide centrata di asterischi
n = 5  # Numero di righe della piramide

for i in range(1, n + 1):
    # Calcoliamo gli spazi prima degli asterischi per centrarli
    spazi = ' ' * (n - i)
    # Stampa gli spazi seguiti dagli asterischi
    print(spazi + '*' * (2 * i - 1))




    *
   ***
  *****
 *******
*********
