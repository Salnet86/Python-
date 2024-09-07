'''
     OLTRE FORMAZIONE PROGRAMMA FIBONACCI
                 ESRCITAZIONE
                 AUTORE SALVO


'''
temp=0
a=0
b=0

print("--Welcome--")
print("-----Fibonacci------")
print("Programma di Fibonacci ")

INPUT=input('Inserisci numero per calcolare Fibonacci ')
count=int(INPUT)
a, b=0,1

for i in  range(count):
    temp=a+b  
    a=b
    b=temp
   # print("Variabile a", a, "Variabile b", b, "Variabile tempo", temp)
    print(f'Fibonacci ={a}')
