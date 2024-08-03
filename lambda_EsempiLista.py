'''
a = [1,2,3,4] 
l = lambda : [print(x) for x in a]
l()
'''
cerca=input('Cerca la frutta')
lis=['mele','feagole','pere','meloni']
Lista=lambda :[lista for lista in lis if lista==cerca] 
Lista()
print(Lista())
   
