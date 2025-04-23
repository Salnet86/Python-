

n=int(input('Inserisci un numero per il calcolo di  tartaglia    :'))

for i in range(n):
    valore = 1
    for j in range(n - i -1):
        print(' ', end=' ')

    for k in range(i+1):
        print(valore, end='   ')
        valore = valore * (i - k) // (k + 1)  

    print()  


