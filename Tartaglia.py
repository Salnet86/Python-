

n=int(input('Inserisci un numero oer il cakcolo di tartaglia   :'))
triangolo=[]

for i in range(n):
    riga=[1] * (i +1)
    for j in range(1 , i):
        riga[j]=triangolo[i-1][j-1] + triangolo[i-1][j]
    triangolo.append(riga)



for tartaglia  in triangolo:
    print(tartaglia)



