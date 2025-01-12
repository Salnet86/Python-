'''
       Esercizio python
           Polidrome 





'''


'''
str="scrivi parola"
flag=False

p=int(len(str)/2)

for i in range(p):
    if str[i]!=str[len(str)-i-1]:
        flag=False
        


if flag:
     print("la frsse e polidrome")
else:
    print("La frase non e polidrome")

print(str)

'''





str=input('Inserisci una frase polidrome      :')
p=len(str)
flag=False
for i in range(len(str)-1,-1,-1):
    if str[i]==str[p - i - 1]:
        flag=True
   
if flag:
    print("La frase e polidrome")
else:
    print("La frase non e polidrome")
