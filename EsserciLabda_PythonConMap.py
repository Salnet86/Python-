from functools import reduce 

'''
     Esercizi lambda python 

'''


'''
lista=[1,2, 4, 5,6, 12]
li=[]
for i in lista:
    calcolo = lambda i:i**2
    li.append(calcolo(i))
print(f'il quadrato di  {lista} e {li}')
'''

'''
numeri = [1,2,3,4,5,6,8,9,10]
out=lambda:[l for l in numeri]
print(out())
'''

#Porenza di dud 
'''
n=[1, 2, 3,4,5,6,7,8,9,10]
squa=list(map(lambda x:x**2,n))
print(squa)

'''
'''
n=[1, 2,3,4,5,6,7,8,9,10]
Filtra=list(filter(lambda x:x%2==0 or x%3==1, n))
print(Filtra)
'''

'''
n=[1, 2 ,3,4,5,6,7,8,9,10]
Reduce=reduce(lambda x, y:x+y, n)
print(Reduce)
'' '