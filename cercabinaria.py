lista=['fragola', 'limone', 'mela','arancio','meloni','anguria','pere' ]

i=len(lista)
j=0


cerca=input('Trova patola     :')
media=int(i/2)
posizione=0
trovata=False




while j < i:
    if j >= media:
        if lista[j]==cerca:
            trovata = True
            posizione = j
    if j <= media:
        if lista[j]==cerca:
            trovata = True
            posizione = j



    j=j+1






if trovata==True:
    print(f'Parola trovata {lista[posizione]}   in posizione { posizione}')
else:
    print('Non ci sono parole frutta nella lista')
